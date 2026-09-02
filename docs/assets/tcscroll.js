/* TCScroll — motor de desplazamiento compartido por las cuatro paginas.
   Vive aparte y no incrustado en cada una a proposito: es el mismo codigo
   para el home, About, Ingredients y Contact, y tenerlo cuatro veces
   garantiza que tarde o temprano se arregla en una y se olvida en las otras.
   Se carga con <script src>; build.py ya recalcula la ruta de assets/ segun
   donde viva cada preview. */

/* ─────────────────────────────────────────────────────────────────────────────
   TCScroll — motor de desplazamiento que funciona DENTRO y FUERA de un iframe.

   El problema (medido en el Wix real el 2026-09-02): dentro de un embed la
   pagina no se desplaza. Wix crea un iframe tan alto como TODO el contenido
   (3.092px), asi que su scrollY es siempre 0, `scroll` no se dispara nunca y
   `window.innerHeight` devuelve el alto del EMBED, no el de la ventana del
   visitante. Las dos animaciones de esta pagina leian las dos cosas, calculaban
   un progreso >= 1 y se quedaban congeladas en el ultimo fotograma: por eso en
   Wix se veian estaticas.

   La solucion: la rueda del raton y el gesto tactil SI llegan al iframe — el
   navegador los entrega al elemento bajo el cursor ANTES de desplazar la pagina
   de arriba. Se acumulan y sirven de posicion aproximada. Es una estimacion, no
   una medida: arrastrar la barra de desplazamiento o pulsar AvPag no generan
   rueda, y ahi la animacion no avanza. Por eso hay una red de seguridad abajo.

   Fuera del iframe (el preview, y cualquier pagina que se desplace de verdad)
   no se toca nada: devuelve pageYOffset e innerHeight igual que siempre.
   ───────────────────────────────────────────────────────────────────────────── */
window.TCScroll=(function(){
  var doc=document.documentElement;
  var subs=[], pend=false, embed=false;

  /* ── Que se ve de verdad ─────────────────────────────────────────────────
     visTop y visH describen QUE FRANJA del embed esta ahora mismo a la vista
     en la ventana del visitante, en coordenadas del propio embed. Las escribe
     el faro (mas abajo) y son una MEDIDA, no una estimacion.
     virt es el acumulador de rueda de la version anterior; solo se usa si el
     faro no llega a funcionar. */
  var visTop=0, visH=0, hayFaro=false;
  var virt=0, tope=0, hubo=false;

  var VENTANA=800, CABECERA=110, RENDIRSE=45000;   // solo para el plan B

  function medir(){
    embed = doc.scrollHeight <= window.innerHeight + 4;
    tope  = Math.max(0, doc.scrollHeight - VENTANA + CABECERA);
  }
  function avisar(){
    if(pend) return; pend=true;
    requestAnimationFrame(function(){ pend=false;
      for(var i=0;i<subs.length;i++){ try{ subs[i](); }catch(e){} } });
  }

  medir();

  /* ── El faro ─────────────────────────────────────────────────────────────
     Aqui esta la clave de todo. Dentro de un iframe de Wix no hay scroll ni
     alto de ventana fiables, pero SI hay una cosa que el navegador calcula
     bien: la interseccion de un elemento con el area visible de VERDAD, ya
     recortada por el viewport de la pagina de arriba. Comprobado el 2026-09-02
     en el banco de pruebas: el hero daba visible=true ratio=0.61 y las
     secciones de mas abajo visible=false, con la pagina padre sin desplazar.

     Observando el propio <body>, `intersectionRect` viene en coordenadas del
     embed: su borde superior ES la posicion del scroll y su alto ES el alto
     real de la ventana. Las dos incognitas que antes tenia que suponer
     (VENTANA=800, CABECERA=110) dejan de hacer falta.

     Los umbrales densos son para que avise a menudo: IntersectionObserver solo
     habla cuando se cruza uno. Entre aviso y aviso interpola la rueda, y el
     siguiente aviso corrige — asi no hay deriva acumulada, que es lo que hacia
     que la animacion fuese bien en un sentido y se quedase pegada en el otro. */
  function encenderFaro(){
    if(!window.IntersectionObserver) return;
    var u=[]; for(var i=0;i<=500;i++) u.push(i/500);
    try{
      new IntersectionObserver(function(es){
        var e=es[es.length-1];
        if(!e.isIntersecting) return;
        var r=e.intersectionRect;
        if(!r || r.height<40) return;      // franja absurda: no fiarse
        hayFaro=true; visTop=r.top; visH=r.height;
        avisar();
      },{threshold:u}).observe(document.body);
    }catch(err){}
  }
  if(embed) encenderFaro();

  /* ── Entradas ────────────────────────────────────────────────────────────
     La rueda, el dedo y el teclado llegan al iframe. Con el faro encendido su
     unico papel es suavizar el tramo entre dos avisos; sin faro son la unica
     fuente y hay que fiarse de ellas. */
  function mover(d){
    if(!embed) return;
    hubo=true;
    if(hayFaro){
      var m=Math.max(0, doc.scrollHeight - visH);
      visTop = visTop+d < 0 ? 0 : (visTop+d > m ? m : visTop+d);
    }else{
      virt = virt+d < 0 ? 0 : (virt+d > tope ? tope : virt+d);
    }
    avisar();
  }

  // Plan B: sin faro, alguien que baje ARRASTRANDO LA BARRA no genera ninguna
  // senal y veria las tarjetas recortadas a cero. Con faro esto sobra, porque
  // el navegador nos dice la verdad haga lo que haga el visitante.
  if(embed) setTimeout(function(){
    if(!hubo && !hayFaro){ virt=tope; avisar(); }
  }, RENDIRSE);

  addEventListener('resize', function(){ medir(); avisar(); }, {passive:true});
  addEventListener('scroll', function(){ if(!embed) avisar(); }, {passive:true});
  addEventListener('wheel',  function(e){
    mover(e.deltaMode===1 ? e.deltaY*16 : e.deltaY);
  }, {passive:true});

  var TECLAS={ArrowDown:120,ArrowUp:-120,PageDown:600,PageUp:-600,
              ' ':600,Spacebar:600,End:99999,Home:-99999};
  addEventListener('keydown', function(e){
    var d=TECLAS[e.key]; if(d!==undefined) mover(d);
  }, {passive:true});

  var ty=0;
  addEventListener('touchstart', function(e){
    if(e.touches[0]) ty=e.touches[0].clientY;
  }, {passive:true});
  addEventListener('touchmove', function(e){
    if(!e.touches[0]) return;
    var y=e.touches[0].clientY; mover(ty-y); ty=y;
  }, {passive:true});

  /* ── Aviso de altura a Wix ───────────────────────────────────────────────
     El contenido no mide lo mismo en cada ancho (2.576px a 1920, 2.543 a 1440,
     2.290 a 1024), asi que ningun alto fijo de caja sirve: si se queda corta
     el iframe crea barra propia y hay dos barras peleando; si sobra, queda
     crema muerta. Aqui se publica la altura real y Velo la recoge con
     onMessage. Si nadie escucha, no pasa nada. */
  function avisarAltura(){
    if(window.self===window.top) return;
    var h=Math.ceil(document.body.getBoundingClientRect().height);
    try{ parent.postMessage({tcAlto:h}, '*'); }catch(e){}
  }
  addEventListener('load', avisarAltura);
  addEventListener('resize', avisarAltura, {passive:true});
  if(window.ResizeObserver){
    try{ new ResizeObserver(avisarAltura).observe(document.body); }catch(e){}
  }

  return {
    // Alto de la ventana del visitante contra el que medir el progreso.
    vh: function(){
      if(!embed) return window.innerHeight;
      return hayFaro ? visH : VENTANA;
    },
    // Distancia del elemento al borde superior de lo que se ve.
    // Fuera del embed es literalmente rect.top. Dentro, rect.top es una
    // constante (el iframe no se desplaza) y hay que restarle donde empieza
    // la franja visible.
    top: function(el){
      var t=el.getBoundingClientRect().top;
      if(!embed) return t;
      return hayFaro ? (t - visTop) : (t + CABECERA - virt);
    },
    on: function(fn){ subs.push(fn); fn(); },
    esEmbed: function(){ return embed; },
    // Para poder mirar por dentro sin adivinar.
    diagnostico: function(){
      return {modo: !embed ? 'pagina' : (hayFaro ? 'embed+faro' : 'embed+rueda'),
              visTop: Math.round(visTop), visH: Math.round(visH),
              virt: Math.round(virt), hubo: hubo};
    }
  };
})();
