#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los embeds de Wix a partir de los archivos de preview.

No se editan a mano: se regeneran. Asi un cambio en un preview se propaga con
`python3 docs/embed/build.py` y no hay que acordarse de replicarlo seis veces.

Cada embed es un documento HTML independiente que Wix carga dentro de un iframe.
De cada preview se quita:
  - el menu (.site-nav), porque el menu lo pone Wix;
  - el andamiaje del preview (sello, panel de opciones, conmutadores);
  - las secciones que van en otra caja o que Michelle pone directamente en Wix.

Y se cambian dos cosas:
  - la fuente Avenir deja de ir incrustada (70 KB por archivo) y pasa a un
    archivo compartido, que el navegador descarga una sola vez;
  - las rutas de los assets se recalculan, porque el embed vive en docs/embed/
    y no donde vivia su preview.
"""

import os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # docs/
SALIDA = os.path.join(RAIZ, 'embed')

# ─────────────────────────────────────────────────────────────────────────────
# Utilidades de recorte
# ─────────────────────────────────────────────────────────────────────────────

def bloque(html, apertura, etiqueta):
    """Devuelve (inicio, fin) del elemento que empieza en `apertura`,
    contando anidamiento de `etiqueta`. Devuelve None si no aparece."""
    i = html.find(apertura)
    if i < 0:
        return None
    abre = re.compile(r'<' + etiqueta + r'\b', re.I)
    cierra = re.compile(r'</' + etiqueta + r'\s*>', re.I)
    prof = 0
    pos = i
    while pos < len(html):
        ma = abre.search(html, pos)
        mc = cierra.search(html, pos)
        if not mc:
            return None
        if ma and ma.start() < mc.start():
            prof += 1
            pos = ma.end()
        else:
            prof -= 1
            pos = mc.end()
            if prof == 0:
                return (i, pos)
    return None


def quitar(html, apertura, etiqueta, obligatorio=True):
    r = bloque(html, apertura, etiqueta)
    if r is None:
        if obligatorio:
            raise SystemExit(f'  !! no encontrado: {apertura[:60]}')
        return html
    return html[:r[0]] + html[r[1]:]


def solo(html, apertura, etiqueta):
    """Extrae el elemento y lo devuelve suelto."""
    r = bloque(html, apertura, etiqueta)
    if r is None:
        raise SystemExit(f'  !! no encontrado: {apertura[:60]}')
    return html[r[0]:r[1]]


# ─────────────────────────────────────────────────────────────────────────────
# Transformaciones comunes
# ─────────────────────────────────────────────────────────────────────────────

FUENTE_EXT = '../assets/avenir-light.otf'

def fuente_externa(html):
    """La fuente incrustada pasa a archivo. 70 KB menos por embed."""
    nuevo, n = re.subn(
        r"src:url\(data:font/[a-z0-9]+;base64,[A-Za-z0-9+/=]+\)",
        f"src:url({FUENTE_EXT})",
        html)
    if n != 1:
        raise SystemExit(f'  !! esperaba 1 fuente incrustada, encontre {n}')
    return nuevo


def sin_menu(html):
    return quitar(html, '<nav class="site-nav"', 'nav')


def sin_andamiaje(html):
    """Fuera todo lo que era solo para revisar en el preview."""
    for ap, et in [('<div id="prev-panel"', 'div'),
                   ('<button type="button" id="prev-fab"', 'button'),
                   ('<div id="prev-badge"', 'div'),
                   ('<div id="hm-tog"', 'div'),
                   ('<div id="pm-tog"', 'div'),
                   ('<div id="vid-tog"', 'div'),
                   ('<div id="ship-tog"', 'div'),
                   ('<div id="ab-tog"', 'div')]:
        html = quitar(html, ap, et, obligatorio=False)
    # el <style> suelto del sello
    html = re.sub(r'<style>#prev-badge\{[^<]*</style>\s*', '', html)
    return html


def rutas(html, origen):
    """Recalcula las rutas de assets segun donde vivia el preview."""
    if origen == 'raiz':
        # docs/_prev-*.html usaba assets/... ; desde docs/embed/ es ../assets/...
        html = re.sub(r'(src|href)="assets/', r'\1="../assets/', html)
        html = re.sub(r'url\(assets/', 'url(../assets/', html)
    elif origen == 'about':
        # about usa DOS raices: ../assets/ (compartida, no cambia) y assets/
        # (la suya propia). Solo se toca la segunda.
        html = re.sub(r'(?<!\.\./)(src|href)="assets/', r'\1="../about/assets/', html)
        html = re.sub(r'(?<!\.\./)url\(assets/', 'url(../about/assets/', html)
    # 'sub' (ingredients, contact) ya usan ../assets/ y siguen a la misma
    # profundidad desde embed/, asi que no hay nada que cambiar.
    return html


# ─────────────────────────────────────────────────────────────────────────────
# Enlaces hacia Wix
# ─────────────────────────────────────────────────────────────────────────────

# Slugs confirmados por Michelle en el panel de SEO de Wix (2026-08-31).
WIX = 'https://www.tcorpi.com'
DESTINOS = {
    'home':        WIX + '/',
    'about':       WIX + '/about-us',
    'ingredients': WIX + '/ingredients',
    'contact':     WIX + '/contact',
}

# Como enlaza cada preview a sus hermanos, segun donde vive.
ENLACES_PREVIEW = {
    # desde docs/            desde docs/<sub>/
    '_prev-ing-v2.html':        'home',
    '../_prev-ing-v2.html':     'home',
    'about/_prev.html':         'about',
    '../about/_prev.html':      'about',
    'ingredients/_prev.html':   'ingredients',
    '../ingredients/_prev.html':'ingredients',
    'contact/_prev.html':       'contact',
    '../contact/_prev.html':    'contact',
}


def _marcar(html, prueba, atributos):
    """Añade atributos a las etiquetas <a> cuyo href pase `prueba`.

    Se inspecciona la etiqueta ENTERA, no solo lo que hay antes del href: los
    botones de WhatsApp ya traian target="_blank" DESPUES del href, y mirando
    solo delante se les añadia un segundo target. El navegador se queda con el
    primero y funciona igual, pero es HTML invalido."""
    def uno(m):
        tag = m.group(0)
        href = re.search(r'href="([^"]*)"', tag)
        if not href or not prueba(href.group(1)):
            return tag
        if 'target=' in tag:
            return tag                      # ya lo trae: no se pisa
        return '<a ' + atributos + tag[2:]
    return re.sub(r'<a\b[^>]*>', uno, html)


def enlaces_wix(html):
    """Los enlaces entre previews pasan a URLs absolutas de Wix con target=_top.

    El target es imprescindible, no cosmetico: un <a> normal dentro de un iframe
    abre el destino DENTRO del iframe, o sea que se veria el sitio de Wix entero
    metido en la cajita del embed. Con _top navega la pestaña completa.
    Comprobado en el Wix real de Michelle el 2026-08-31: Wix lo permite, asi que
    no hace falta el rodeo por Velo.

    Se ordena de mas largo a mas corto para que '../about/_prev.html' se procese
    antes que 'about/_prev.html' y no quede un '../' suelto delante de la URL."""
    for viejo in sorted(ENLACES_PREVIEW, key=len, reverse=True):
        html = html.replace('href="' + viejo + '"',
                            'href="' + DESTINOS[ENLACES_PREVIEW[viejo]] + '"')
    # No se exige que haya enlaces: home-3 es solo el carril de testimonios y no
    # tiene ninguno. Lo que si es un fallo es que quede alguno SIN reescribir,
    # porque apuntaria a un archivo de preview que no existe en el servidor.
    resto = re.findall(r'href="[^"]*_prev[^"]*"', html)
    if resto:
        raise SystemExit(f'  !! enlaces de preview sin reescribir: {resto[:3]}')
    html = _marcar(html, lambda h: h.startswith(WIX), 'target="_top"')
    return html, len(re.findall(re.escape(WIX), html))


def enlaces_externos(html):
    """WhatsApp abre en pestaña nueva; no tiene sentido sacar al visitante del
    sitio. mailto: y sms: van con _top porque desde un iframe pueden quedar
    bloqueados."""
    html = _marcar(html, lambda h: h.startswith('https://wa.me/'),
                   'target="_blank" rel="noopener"')
    html = _marcar(html, lambda h: h.startswith(('mailto:', 'sms:')), 'target="_top"')
    return html


def sin_costura(html, reglas):
    """Quita el relleno de los BORDES del embed.

    Dos razones distintas:

    1. «Why buyers choose» y «Trusted partners» eran UNA sola seccion en el
       original — el verde corria continuo entre las dos. Al partirlas cada
       mitad se quedo con su relleno, y al apilarlas en Wix se suman: 80px de
       una mas 120px de la otra, mas lo que ponga Wix encima.

    2. El aire ENTRE secciones lo pone Wix. Si lo ponen los dos, va doble.

    Solo se tocan los bordes que dan a otra caja: el relleno interior se
    respeta, y en las secciones con fondo de color el que queda dentro tiene
    que seguir ahi o el color no llena el hueco."""
    extra = '\n/* Bordes del embed: el aire entre cajas lo pone Wix (build.py) */\n' + reglas + '\n'
    i = html.rindex('</style>')
    return html[:i] + extra + html[i:]


def autoplay_home2(html):
    """Las dos animaciones de home-2 pasan de scroll a tiempo.

    Dentro de un iframe el scroll de la pagina de Wix NO llega (medido: el
    scrollY del embed se queda en 0 mientras el padre se desplaza), asi que
    ambas se quedaban congeladas en su primer fotograma: el titulo pequeno y la
    seccion «Why» sin teñir de verde, con las tarjetas sin desplegar.

    No hace falta desmontar los oyentes de scroll que ya hay: como no se dispara
    ningun evento de scroll dentro del iframe, nunca vuelven a escribir. Este
    bucle simplemente pinta encima."""
    js = """
<script>
/* Reproduccion por tiempo — sustituye al scroll dentro del embed (build.py) */
(function(){
  var sec   = document.querySelector('.ingredients');
  var title = sec && sec.querySelector('.ing-title');
  var why   = document.getElementById('why');
  var cards = why ? [].slice.call(why.querySelectorAll('.why-card')) : [];
  if(!title && !why) return;

  function fin(){
    if(title) title.style.setProperty('--tsc','1');
    if(window.applyWhyFrame) window.applyWhyFrame(1);
    cards.forEach(function(c){ c.style.clipPath='none'; });
  }
  if(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches){
    fin(); return;
  }

  var DUR=1500, t0=null;
  function easeOut(x){ return 1-Math.pow(1-x,3); }
  function tramo(p,a,b){ var k=(p-a)/(b-a); return k<0?0:k>1?1:k; }

  function paso(ts){
    if(t0===null) t0=ts;
    var p=(ts-t0)/DUR;
    if(p>=1){ fin(); return; }
    var k=easeOut(p);
    if(title) title.style.setProperty('--tsc',(0.74+0.26*k).toFixed(4));
    if(window.applyWhyFrame) window.applyWhyFrame(easeOut(tramo(p,0.10,0.70)));
    cards.forEach(function(c,i){
      var ck=easeOut(tramo(p, 0.30+i*0.10, 0.85+i*0.10));
      c.style.clipPath='inset(0 0 '+((1-ck)*100).toFixed(1)+'% 0 round 24px)';
    });
    requestAnimationFrame(paso);
  }
  requestAnimationFrame(paso);
  // Red de seguridad: si rAF no corre (pestaña de fondo), nada puede quedarse
  // a medio pintar — el verde a medias o una tarjeta recortada se ven rotos.
  setTimeout(function(){ if(t0===null) fin(); }, 2500);
})();
</script>
"""
    i = html.rindex('</body>')
    return html[:i] + js + html[i:]


def titulo(html, t):
    return re.sub(r'<title>[^<]*</title>', f'<title>{t}</title>', html, count=1)


def cabecera(html, nombre):
    aviso = (f'<!-- GENERADO por docs/embed/build.py desde el preview.\n'
             f'     NO editar a mano: los cambios se pierden al regenerar.\n'
             f'     Embed: {nombre} -->\n')
    return aviso + html


# ─────────────────────────────────────────────────────────────────────────────
# Recetas
# ─────────────────────────────────────────────────────────────────────────────

def build_contact():
    h = open(os.path.join(RAIZ, 'contact/_prev.html'), encoding='utf-8').read()
    h = sin_menu(h); h = sin_andamiaje(h)
    # El titulo y los dos botones los pone Michelle en Wix.
    h = quitar(h, '<header class="head">', 'header')
    h = rutas(h, 'sub'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'Contact — TradeCorp')
    return cabecera(h, 'contact')


def build_ingredients():
    h = open(os.path.join(RAIZ, 'ingredients/_prev.html'), encoding='utf-8').read()
    h = sin_menu(h); h = sin_andamiaje(h)
    # El titulo lo pone Michelle en Wix.
    h = quitar(h, '<h1 class="title">', 'h1')
    h = rutas(h, 'sub'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'Ingredients — TradeCorp')
    return cabecera(h, 'ingredients')


# Los conmutadores del preview se borran del HTML, pero su script sigue en el
# archivo y engancha listeners a botones que ya no existen -> TypeError y el
# resto del script no llega a correr. Hay que quitar esas tres sentencias.
# Las que usan querySelectorAll son inofensivas: una lista vacia no falla.
LISTENERS_MUERTOS = [
 " document.getElementById('pm-replay').addEventListener('click',function(){ repetir(pil); });\n",
 """ var fab=document.getElementById('prev-fab');
 fab.addEventListener('click',function(){
   var abierto=d.classList.toggle('prev-open');
   fab.setAttribute('aria-expanded',String(abierto));
   fab.textContent=abierto?'Cerrar':'Opciones';
 });
""",
 """ document.getElementById('hm-replay').addEventListener('click',function(){
   descubierto=false; repetir(grid,pista); });
""",
]

def sin_listeners_muertos(html):
    for frag in LISTENERS_MUERTOS:
        if frag not in html:
            raise SystemExit('  !! listener muerto no encontrado: ' + frag[:50])
        html = html.replace(frag, '')
    return html


def sin_css_conmutadores(html):
    """El CSS de los conmutadores ya no apunta a nada."""
    for sel in ('#hm-tog', '#pm-tog', '#vid-tog', '#ship-tog', '#ab-tog',
                '#prev-fab', '#prev-panel'):
        html = re.sub(r'^[^\n]*' + re.escape(sel) + r'[^\n]*\{[^}]*\}[^\n]*$\n?',
                      '', html, flags=re.M)
    return html


def build_about():
    h = open(os.path.join(RAIZ, 'about/_prev.html'), encoding='utf-8').read()
    h = sin_menu(h); h = sin_andamiaje(h)
    # Direcciones B y C: descartadas. Se BORRAN, no se ocultan — si se quedan,
    # sus <h1> viajan a la web y la pagina acaba con tres.
    h = quitar(h, '<div class="ab ab-b"', 'div')
    h = quitar(h, '<div class="ab ab-c"', 'div')
    # "Tell us what you need" lo pone Michelle en Wix.
    h = quitar(h, '<div class="abA-end">', 'div')
    h = sin_listeners_muertos(h); h = sin_css_conmutadores(h)
    h = rutas(h, 'about'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'Who we are — TradeCorp')
    return cabecera(h, 'about')


# ─────────────────────────────────────────────────────────────────────────────
# El home, partido en las tres secciones que pidio Michelle
# ─────────────────────────────────────────────────────────────────────────────

def sin_guion(html, marcador):
    """Borra el <script> completo que contiene `marcador`.

    Hace falta porque un guion sin su seccion no falla en silencio: revienta con
    TypeError en la primera linea que busca un elemento que ya no esta, y el
    resto del archivo se queda sin ejecutar."""
    i = html.find(marcador)
    if i < 0:
        raise SystemExit(f'  !! marcador no encontrado: {marcador[:50]}')
    ini = html.rindex('<script>', 0, i)
    fin = html.index('</script>', i) + len('</script>')
    return html[:ini] + html[fin:]


# El guion del intro empieza leyendo los elementos del hero por id. Sin ellos,
# `zoom.querySelector` lanza TypeError y ahi muere el archivo entero.
GUION_INTRO = "var stage=document.getElementById('stage'),"
GUION_WHY   = "/* Why TradeCorp? — scroll-driven curved reveal"


def _home():
    return open(os.path.join(RAIZ, '_prev-ing-v2.html'), encoding='utf-8').read()


def build_home_1():
    """Logo creciendo + hero + los 4 valores.

    El intro ya corre solo al cargar (html.intro-auto), que es lo que lo hace
    viable dentro de Wix: el scroll de la pagina padre no llega al iframe."""
    h = _home()
    h = sin_menu(h); h = sin_andamiaje(h)
    h = quitar(h, '<section class="ingredients"', 'section')
    h = quitar(h, '<section class="why"', 'section')
    h = sin_costura(h, '.track{padding-bottom:0}')
    h = rutas(h, 'raiz'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'TradeCorp')
    return cabecera(h, 'home-1')


def build_home_2():
    """Most requested ingredients + Why Buyers Choose TradeCorp."""
    h = _home()
    h = sin_menu(h); h = sin_andamiaje(h)
    h = quitar(h, '<div class="track" id="track">', 'div')
    # Trusted partners se va a su propia caja
    h = quitar(h, '<div class="tp">', 'div')
    h = quitar(h, '<div class="tp-marquee"', 'div')
    h = sin_guion(h, GUION_INTRO)          # aqui no hay hero que animar
    h = sin_costura(h, '.ingredients{padding-top:0}\n.why{padding-bottom:0}')
    h = autoplay_home2(h)
    h = rutas(h, 'raiz'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'Our ingredients — TradeCorp')
    return cabecera(h, 'home-2')


def build_home_3():
    """Trusted partners, solo el titulo y el carril."""
    h = _home()
    h = sin_menu(h); h = sin_andamiaje(h)
    h = quitar(h, '<div class="track" id="track">', 'div')
    h = quitar(h, '<section class="ingredients"', 'section')
    # De la seccion "why" sobrevive unicamente el bloque de testimonios.
    h = quitar(h, '<div class="why-curve"', 'div')
    h = quitar(h, '<h2 class="why-title">', 'h2')
    h = quitar(h, '<span class="why-title-line">', 'span')
    h = quitar(h, '<div class="why-grid">', 'div')
    # Sin tarjetas que desplegar, el guion del scrub no pinta nada — y ademas
    # dejaria el fondo a medio camino entre crema y salvia, porque su unica
    # lectura inicial depende de una posicion de scroll que aqui no existe.
    # Fuera el guion: manda el `background:var(--salvia)` del CSS.
    h = sin_guion(h, GUION_WHY)
    h = sin_guion(h, GUION_INTRO)          # aqui no hay hero que animar
    h = sin_costura(h, '.why{padding-top:0}')
    h = rutas(h, 'raiz'); h = fuente_externa(h)
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = titulo(h, 'Trusted partners — TradeCorp')
    return cabecera(h, 'home-3')


def build_home_entero():
    """El home completo en una sola caja — para comparar contra las tres.

    OJO con el hero: mide 100vh, y dentro de un iframe `vh` es el alto del
    IFRAME, no el de la pantalla. En una caja de 2.600px el hero se estira a
    2.600px."""
    h = _home()
    h = sin_menu(h); h = sin_andamiaje(h)
    h = autoplay_home2(h)
    # El hero mide 100vh, y dentro de un iframe `vh` es el alto del IFRAME: en
    # una caja de 2.600px el hero se estiraba a 2.600px (medido). Se le fija un
    # alto en px. No se pierde nada frente a las tres cajas: alli `100vh`
    # tampoco seguia la pantalla del visitante, seguia el alto que Michelle le
    # daba a la seccion — este es el mismo numero, escrito de forma explicita.
    # OJO: no basta con fijar .track. El lienzo del intro es .stage, que lleva
    # `height:100vh` propio, y dentro del iframe eso son 3.092px: .zoom (el SVG
    # del logo) y .card (la caja verde del hero) heredan ese alto por `inset:0`.
    # Resultado medido el 2026-09-02: el logo se dibujaba a 3,4x su tamano y el
    # verde llenaba la pantalla entera. Se fijan LOS DOS al mismo numero.
    # 780 y no 900: el contenido del hero termina en 719px (copy + banda de
    # valores), asi que 900 dejaba 180px de crema muerta antes de
    # "Our most requested ingredients" — el hueco que reporto Michelle.
    ALTO, ALTO_MOVIL = 780, 760
    _t = ('.track,html.intro-auto .track,html.intro-collapsed .track,'
          'html:not(.intro-armed) .track')
    h = sin_costura(h, '%s{height:%dpx}\n.stage{height:%dpx}\n'
                       '@media (max-width:640px){%s{height:%dpx}\n'
                       '.stage{height:%dpx}}'
                       % (_t, ALTO, ALTO, _t, ALTO_MOVIL, ALTO_MOVIL))
    h, _n = enlaces_wix(h); h = enlaces_externos(h)
    h = rutas(h, 'raiz'); h = fuente_externa(h)
    h = titulo(h, 'TradeCorp')
    return cabecera(h, 'home-entero')


RECETAS = {
    'home-entero': build_home_entero,
    'home-1': build_home_1,
    'home-2': build_home_2,
    'home-3': build_home_3,
    'contact': build_contact,
    'ingredients': build_ingredients,
    'about': build_about,
}

if __name__ == '__main__':
    pedidos = sys.argv[1:] or list(RECETAS)
    for nombre in pedidos:
        if nombre not in RECETAS:
            print(f'  ?? receta desconocida: {nombre}'); continue
        html = RECETAS[nombre]()
        destino = os.path.join(SALIDA, nombre + '.html')
        open(destino, 'w', encoding='utf-8').write(html)
        print(f'  {nombre + ".html":<22} {len(html.encode()):>8,} bytes')
