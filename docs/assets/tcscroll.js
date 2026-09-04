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
/* ─────────────────────────────────────────────────────────────────────────────
   Videos que no aparezcan de golpe (movil)

   Un <video> no pinta nada hasta que decodifica su primer fotograma, y entonces
   aparece de golpe — a veces un segundo largo despues de que el resto de la
   pagina ya este puesta. En un telefono, con la conexion mas lenta, se nota
   mucho: primero el marco vacio, luego un salto.

   Se atenua con `filter:opacity()` y NO con `opacity` a secas. Es a proposito:
   la opacidad de los dos videos del hero de About la escribe el encadenado por
   JS en cada fotograma (.hv-a / .hv-b), y si los dos escribieran la misma
   propiedad se pelearian. `filter` y `opacity` se multiplican, asi que conviven
   sin tocarse.

   La regla que oculta se inyecta desde AQUI y no desde la hoja de estilos: si
   este guion no llega a correr, los videos se ven — nunca al reves.
   Y hay plazo de 3s por si el video no llega a tener datos (red caida, formato
   no soportado): mostrarlo sin transicion es mucho mejor que no mostrarlo.
   ───────────────────────────────────────────────────────────────────────────── */
(function(){
  var vids=[].slice.call(document.querySelectorAll('video'));
  if(!vids.length) return;
  if(!(window.matchMedia && matchMedia('(max-width:720px)').matches)) return;

  var st=document.createElement('style');
  st.textContent='video{filter:opacity(0);transition:filter .6s ease}'+
                 'video.tc-listo{filter:opacity(1)}';
  document.head.appendChild(st);

  vids.forEach(function(v){
    var puesto=false;
    function ver(){ if(puesto) return; puesto=true; v.classList.add('tc-listo'); }
    if(v.readyState>=2){ ver(); return; }          // ya tenia datos
    v.addEventListener('loadeddata', ver, {once:true});
    v.addEventListener('canplay',    ver, {once:true});
    v.addEventListener('error',      ver, {once:true});
    setTimeout(ver, 3000);
  });
})();

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
    // `self !== top` PRIMERO, y la comparacion de alturas solo como respaldo.
    // Comparar alturas era una carrera perdida: Wix fija el alto de la caja
    // DESPUES de cargar (Velo lo recibe por onMessage), asi que en el primer
    // medir() scrollHeight todavia era mayor que innerHeight, embed salia
    // false, el faro no se encendia nunca y `top()` devolvia un rect.top que
    // dentro del iframe es constante. Progreso siempre igual = animacion
    // congelada en el ultimo fotograma. Medido el 2026-09-04 en el banco:
    // modo "pagina" y vh 2543 (el alto del embed entero) en vez de 741.
    // Dentro de un iframe SIEMPRE es un embed; no hay nada que deducir.
    embed = (window.self !== window.top) || doc.scrollHeight <= window.innerHeight + 4;
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

     OJO: observar el propio <body> NO sirve, aunque lo pareciera. Dentro del
     iframe el body SIEMPRE intersecta, asi que el observador habla una vez y
     no vuelve, y su intersectionRect no da la franja visible (medido el
     2026-09-04: visH=0 y vh() devolvia el alto del embed entero). Por eso las
     animaciones quedaban congeladas en el ultimo fotograma.
     Lo que SI cruza la frontera de un iframe de otro origen es el
     `isIntersecting` de cada elemento — es la base de las APIs de visibilidad
     de anuncios. Asi que se siembra una ESCALERA de testigos de 1px cada 20:
     los que estan a la vista dicen donde empieza y donde acaba la franja
     visible, con resolucion de 20px. Entre peldano y peldano interpola la
     rueda, y el siguiente peldano corrige.

     Los umbrales densos son para que avise a menudo: IntersectionObserver solo
     habla cuando se cruza uno. Entre aviso y aviso interpola la rueda, y el
     siguiente aviso corrige — asi no hay deriva acumulada, que es lo que hacia
     que la animacion fuese bien en un sentido y se quedase pegada en el otro. */
  var faroPuesto=false;
  var PASO=20, testigos=[], escalera=null, vistos={};

  function sembrar(){
    if(escalera && escalera.parentNode) escalera.parentNode.removeChild(escalera);
    testigos=[]; vistos={};
    escalera=document.createElement('div');
    escalera.setAttribute('aria-hidden','true');
    escalera.style.cssText='position:absolute;top:0;left:0;width:1px;height:0;'+
                           'pointer-events:none;z-index:-1;overflow:visible';
    var n=Math.ceil(doc.scrollHeight/PASO);
    for(var i=0;i<n;i++){
      var t=document.createElement('div');
      t.style.cssText='position:absolute;left:0;width:1px;height:1px;top:'+(i*PASO)+'px';
      t.setAttribute('data-i', i);
      escalera.appendChild(t); testigos.push(t);
    }
    document.body.appendChild(escalera);
    return n;
  }

  function encenderFaro(){
    if(faroPuesto || !window.IntersectionObserver) return;
    faroPuesto=true;
    var n=sembrar(), io;
    try{
      io=new IntersectionObserver(function(es){
        for(var i=0;i<es.length;i++){
          var k=es[i].target.getAttribute('data-i');
          if(k===null) continue;
          if(es[i].isIntersecting) vistos[k]=1; else delete vistos[k];
        }
        var min=Infinity, max=-1;
        for(var j in vistos){ var v=+j; if(v<min)min=v; if(v>max)max=v; }
        if(max<0) return;                      // nada a la vista: no tocar
        hayFaro=true;
        visTop=min*PASO;
        visH=(max-min+1)*PASO;
        avisar();
      });
    }catch(err){ return; }
    for(var i=0;i<n;i++) io.observe(testigos[i]);
    faroIO=io;
  }
  var faroIO=null;
  // Resembrar cuando cambia el alto: los peldanos son posiciones absolutas y si
  // el contenido crece (el catalogo con un filtro, por ejemplo) faltarian abajo.
  var altoSembrado=0;
  function revisarEscalera(){
    if(!faroPuesto) return;
    var h=doc.scrollHeight;
    if(Math.abs(h-altoSembrado) < PASO*4) return;
    altoSembrado=h;
    if(faroIO){ try{ faroIO.disconnect(); }catch(e){} }
    faroPuesto=false; faroIO=null;
    encenderFaro();
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

  // El modo se vuelve a mirar, no se decide una sola vez: si algo cambia el
  // alto de la caja despues de cargar, el faro se enciende en cuanto procede.
  function revisarModo(){
    var antes=embed;
    medir();
    if(embed) encenderFaro();
    revisarEscalera();
    if(embed!==antes) avisar();
  }
  addEventListener('load', revisarModo);
  setInterval(revisarModo, 500);

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
  var ultimoAlto=-1;
  function avisarAltura(){
    if(window.self===window.top) return;
    var h=Math.ceil(document.body.getBoundingClientRect().height);
    if(h===ultimoAlto || h<1) return;   // no repetir lo mismo
    ultimoAlto=h;
    try{ parent.postMessage({tcAlto:h}, '*'); }catch(e){}
  }
  addEventListener('load', avisarAltura);
  addEventListener('resize', avisarAltura, {passive:true});
  if(window.ResizeObserver){
    try{ new ResizeObserver(avisarAltura).observe(document.body); }catch(e){}
  }
  // Ademas del observador, un repaso cada medio segundo. Parece redundante y no
  // lo es: el ResizeObserver se estrangula igual que rAF cuando la pestana esta
  // en segundo plano, y en el catalogo de ingredientes la altura cambia de 8.308
  // a 783 con un filtro. Si ese aviso se pierde, la caja de Wix se queda con el
  // alto viejo y reaparece la segunda barra. Comparar dos numeros dos veces por
  // segundo no cuesta nada, y solo se publica cuando cambia de verdad.
  setInterval(avisarAltura, 500);

  /* ── Puente para las ventanas emergentes de Wix ──────────────────────────
     Michelle incrusto los formularios en lightboxes de Wix. Un boton que vive
     DENTRO de este iframe no puede abrirlos: el lightbox lo dibuja la pagina de
     Wix y desde aqui no hay forma de pedirselo. Lo unico que cruza la frontera
     es postMessage, asi que va por el mismo canal que la altura.

     El plan B es lo importante: si Velo no esta puesto en esa pagina, o falla,
     el <a> conserva su href al formulario en wixforms.com y el visitante llega
     igual. Nunca un boton muerto.

     Por eso NO se intercepta el clic a ciegas: Velo avisa al cargar con
     {tcVelo:1} y solo a partir de ahi se abre el lightbox. Sin ese saludo, el
     enlace se comporta como un enlace normal. */
  var veloListo=false;
  addEventListener('message', function(e){
    if(e && e.data && e.data.tcVelo) veloListo=true;
  });

  addEventListener('click', function(e){
    if(!veloListo) return;                       // sin Velo, manda el href
    var a=e.target && e.target.closest && e.target.closest('a[data-tc-form]');
    if(!a) return;
    // Respetar los gestos de "abrir en otra parte": si el visitante pide una
    // pestaña nueva a proposito, no se le roba el clic.
    if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button!==0) return;
    e.preventDefault();
    try{ parent.postMessage({tcAbrir:a.getAttribute('data-tc-form')}, '*'); }catch(err){}
  });

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
    // Para poder DARSE DE BAJA. Una animacion que ya termino no tiene nada que
    // recalcular, y sin esto seguia corriendo en cada gesto durante el resto de
    // la visita: cuatro getBoundingClientRect y cuatro escrituras de estilo por
    // fotograma, por cada animacion terminada. Es parte del «se traba».
    off: function(fn){
      for(var i=subs.length-1;i>=0;i--) if(subs[i]===fn) subs.splice(i,1);
    },
    esEmbed: function(){ return embed; },
    // Para poder mirar por dentro sin adivinar.
    diagnostico: function(){
      return {modo: !embed ? 'pagina' : (hayFaro ? 'embed+faro' : 'embed+rueda'),
              visTop: Math.round(visTop), visH: Math.round(visH),
              virt: Math.round(virt), hubo: hubo};
    }
  };
})();
