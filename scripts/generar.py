#!/usr/bin/env python3
"""Genera las páginas HTML de la web del Festival Latino Villa de Teror
en español (raíz), inglés (/en/) y francés (/fr/).

Uso:  python3 scripts/generar.py
- Textos de la web:            scripts/textos.py
- Noticias, carteles y próxima edición: data/*.json (se editan desde el portal; ver scripts/datos.py)
- Traducciones de noticias:    scripts/noticias_traducidas.py
El resultado son ficheros .html estáticos (lo que publica Cloudflare).
No edites los .html a mano: se sobrescriben.
"""
import html
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from iconos import CLAVE, ICO  # noqa: E402
from datos import carteles, noticias, proxima  # noqa: E402
from noticias_traducidas import TRADUCCIONES  # noqa: E402
from textos import IDIOMAS, MESES, RUTAS, T  # noqa: E402

DOMINIO = "https://festivallatinoteror.es"
EMAIL = "festivallatinoteror@gmail.com"
EMAIL_PRENSA = "prensa@teror.es"
INSTAGRAM = "https://www.instagram.com/flvteror/"
NOTICIAS = noticias()
PROXIMA = proxima()
FACEBOOK = "https://www.facebook.com/flvteror"


def esc(t):
    return html.escape(t, quote=True)


def fecha_larga(iso, lang):
    a, m, d = iso.split("-")
    mes = MESES[lang][int(m) - 1]
    if lang == "en":
        return f"{int(d)} {mes} {a}"
    if lang == "fr":
        return f"{int(d)} {mes} {a}"
    return f"{int(d)} de {mes} de {a}"


def img(ruta, alt, anchos, sizes, clase="", carga="lazy", prioridad=False):
    srcset = ", ".join(f"/{ruta}-{w}.webp {w}w" for w in anchos)
    extra = ' fetchpriority="high"' if prioridad else ""
    c = f' class="{clase}"' if clase else ""
    return (f'<img src="/{ruta}-{anchos[0]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'alt="{esc(alt)}" loading="{carga}" decoding="async"{extra}{c}>')


def noticia_en(n, lang):
    """La noticia con los campos traducidos al idioma (o en español si no hay traducción)."""
    if lang == "es":
        return n
    tr = TRADUCCIONES.get(n["slug"], {}).get(lang)
    return {**n, **tr} if tr else n


def url_noticia(slug, lang):
    return f'{RUTAS[lang]["noticias"]}{slug}.html'


# ---------------------------------------------------------------- plantilla
def cabecera(lang, seccion, alternas):
    t, base = T[lang], RUTAS[lang]["base"]
    hrefs = [f"{base}#edicion-30", RUTAS[lang]["noticias"], f"{base}#ediciones",
             f"{base}#sostenibilidad", f"{base}#teror", f"{base}#contacto"]
    items = []
    for i, (href, texto) in enumerate(zip(hrefs, t["menu"])):
        cur = ' aria-current="page"' if (seccion == "noticias" and i == 1) else ""
        items.append(f'<li><a href="{href}"{cur}>{texto}</a></li>')
    idiomas = []
    for l in IDIOMAS:
        if l == lang:
            idiomas.append(f'<li><span aria-current="true" lang="{l}" title="{T[l]["nombre_idioma"]}">{T[l]["corto"]}</span></li>')
        else:
            idiomas.append(f'<li><a href="{alternas[l]}" hreflang="{l}" lang="{l}" title="{T[l]["nombre_idioma"]}">{T[l]["corto"]}</a></li>')
    franja = ""
    if PROXIMA.get("fechas") or PROXIMA.get("aviso"):
        rotulo = {"es": "Próxima edición", "en": "Next edition", "fr": "Prochaine édition"}[lang]
        texto = esc(PROXIMA.get("aviso") or f'{rotulo} · <strong>{PROXIMA["fechas"]}</strong> · Plaza de Sintes, Teror')
        texto = texto.replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>")
        franja = f'<div class="franja-proxima"><div class="contenedor"><p>{ICO["cal"]}<span>{texto}</span></p></div></div>\n'
    return f'''<a class="saltar" href="#contenido">{t["saltar"]}</a>
{franja}<header class="nav">
  <div class="contenedor">
    <a class="marca" href="{base}" aria-label="{esc(t["ir_inicio"])}"><span class="marca-num" aria-hidden="true">30</span><span>Festival Latino<small>Villa de Teror</small></span></a>
    <div class="nav-derecha">
      <ul class="idiomas" aria-label="{t["idioma"]}">{"".join(idiomas)}</ul>
      <button class="boton-menu" type="button" aria-controls="menu" aria-expanded="false"><span class="visualmente-oculto">{t["abrir_menu"]}</span>{ICO["menu"]}</button>
    </div>
    <ul class="menu" id="menu">{"".join(items)}</ul>
  </div>
</header>'''


def pie(lang):
    t = T[lang]
    nota = t["legal_nota"]
    leg = t["legal"]
    return f'''<footer class="pie">
  <div class="contenedor">
    <div class="pie-arriba">
      <div class="pie-org">
        <img src="/img/logos/ayuntamiento-teror.webp" alt="Ayuntamiento de Teror" width="151" height="80" loading="lazy">
        <span>{t["pie_org"]}</span>
      </div>
      <div class="pie-redes">
        <a href="{INSTAGRAM}" rel="noopener" aria-label="{esc(t["pie_ig"])}">{ICO["ig"]}</a>
        <a href="{FACEBOOK}" rel="noopener" aria-label="{esc(t["pie_fb"])}">{ICO["fb"]}</a>
        <a href="mailto:{EMAIL}" aria-label="{esc(t["pie_mail"])}">{ICO["mail"]}</a>
      </div>
    </div>
    <div class="pie-base">
      <span>© <span id="anio">2026</span> Ayuntamiento de Teror · Festival Latino Villa de Teror</span>
      <span><a href="/aviso-legal.html" hreflang="es">{leg[0]}</a> · <a href="/privacidad.html" hreflang="es">{leg[1]}</a> · <a href="/cookies.html" hreflang="es">{leg[2]}</a>{nota}</span>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>'''


def pagina(lang, titulo, descripcion, ruta, cuerpo, alternas, seccion="inicio",
           og_img="/img/og-festival-latino-teror.jpg", tipo="website", extra_head=""):
    canon = DOMINIO + ruta
    hreflang = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMINIO}{alternas[l]}">\n' for l in IDIOMAS)
    if len(set(alternas.values())) > 1:
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{DOMINIO}{alternas["es"]}">\n'
    else:
        hreflang = ""
    otros_locales = "".join(f'<meta property="og:locale:alternate" content="{T[l]["locale"]}">\n'
                            for l in IDIOMAS if l != lang) if hreflang else ""
    return f'''<!doctype html>
<html lang="{lang}" class="sin-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(descripcion)}">
<link rel="canonical" href="{canon}">
{hreflang}<meta name="theme-color" content="#2a0716">
<meta property="og:type" content="{tipo}">
<meta property="og:site_name" content="Festival Latino Villa de Teror">
<meta property="og:locale" content="{T[lang]["locale"]}">
{otros_locales}<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(descripcion)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMINIO}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/barlow-condensed-latin-800-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/barlow-condensed-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/estilos.css">
{extra_head}</head>
<body>
{cabecera(lang, seccion, alternas)}
<main id="contenido">
{cuerpo}
</main>
{pie(lang)}
</body>
</html>
'''


def tarjeta_noticia(n, lang):
    n = noticia_en(n, lang)
    return f'''<a class="noticia aparece" href="{url_noticia(n["slug"], lang)}">
  {img(n["imagen"], n["imagen_alt"], n["anchos"], "(max-width:620px) 100vw, (max-width:980px) 50vw, 380px")}
  <div class="noticia-cuerpo">
    <time datetime="{n["fecha"]}">{fecha_larga(n["fecha"], lang)}</time>
    <h3>{esc(n["titulo"])}</h3>
    <p>{esc(n["resumen"])}</p>
    <span class="leer">{T[lang]["leer"]}</span>
  </div>
</a>'''


# ---------------------------------------------------------------- inicio
# Archivo de carteles: (año, edición, imagen, anchos, cabezas de cartel, slug de noticia) desde data/carteles.json
ARCHIVO = carteles()

ICONOS_RASGOS = ["mic", "baile", "abierto", "huella"]
ICONOS_EJES = ["bus", "gota", "recicla", "manos"]


def inicio(lang):
    t, base = T[lang], RUTAS[lang]["base"]
    alternas = {l: RUTAS[l]["base"] for l in IDIOMAS}

    galeria = ""
    for anio, num, ruta, anchos, cabeza, slug in ARCHIVO:
        foto = img(ruta, t["alt_cartel_ed"].format(num=num, anio=anio), anchos,
                   "(max-width:620px) 50vw, (max-width:980px) 33vw, 280px")
        pie_txt = f'<span class="cartel-anio">{anio} · {num}</span><span class="cartel-cabeza">{cabeza}</span>'
        fig = f"<figure>{foto}<figcaption>{pie_txt}</figcaption></figure>"
        galeria += f'<li class="aparece"><a href="{url_noticia(slug, lang)}">{fig}</a></li>' if slug else f'<li class="aparece">{fig}</li>'

    ritmos = "".join(f"<span>{r}</span>" for r in t["ritmos"])
    cifras = "".join(f'<li class="cifra aparece"><strong>{a}</strong><span>{b}</span></li>' for a, b in t["cifras"])
    dias = ""
    for i, (cuando, h3, p, lista) in enumerate(t["dias"]):
        clase = "dia destacado aparece" if i == 2 else "dia aparece"
        lis = "".join(f"<li>{x}</li>" for x in lista)
        dias += f'<article class="{clase}"><p class="dia-cuando">{cuando}</p><h3>{h3}</h3><p>{p}</p><ul>{lis}</ul></article>'
    rasgos = "".join(f'<li class="rasgo aparece"><div class="icono">{ICO[ic]}</div><h3>{h}</h3><p>{p}</p></li>'
                     for ic, (h, p) in zip(ICONOS_RASGOS, t["rasgos"]))
    ejes = "".join(f'<li class="eje aparece">{ICO[ic]}<h3>{h}</h3><p>{p}</p></li>'
                   for ic, (h, p) in zip(ICONOS_EJES, t["ejes"]))
    noticias = "".join(tarjeta_noticia(n, lang) for n in NOTICIAS[:3])

    ld = {
        "@context": "https://schema.org", "@type": "Festival",
        "name": "30.º Festival Latino Villa de Teror", "startDate": "2026-07-20", "endDate": "2026-07-25",
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "isAccessibleForFree": True, "inLanguage": lang,
        "location": {"@type": "Place", "name": "Plaza de Sintes",
                     "address": {"@type": "PostalAddress", "addressLocality": "Teror", "postalCode": "35330",
                                 "addressRegion": "Las Palmas", "addressCountry": "ES"}},
        "image": [DOMINIO + "/img/og-festival-latino-teror.jpg"],
        "description": t["descripcion"],
        "organizer": {"@type": "Organization", "name": "Ayuntamiento de Teror", "url": "https://teror.es"},
        "performer": [{"@type": "MusicGroup", "name": n} for n in ["Tony y Mimy Succar", "Tromboranga", "La Golosina"]],
    }
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'

    cuerpo = f'''
<section class="portada" aria-labelledby="titulo-portada">
  <div class="contenedor">
    <div class="portada-texto">
      <p class="etiqueta">{t["etiqueta"]}</p>
      <h1 class="titular" id="titulo-portada"><span class="fino">{t["h1_fino"]}</span><span class="grande">Festival Latino</span><span class="villa">{t["h1_villa"]}</span></h1>
      <p class="portada-lema">{t["lema"]}</p>
      <ul class="datos-portada">
        <li>{ICO["cal"]} {t["fechas"]}</li>
        <li>{ICO["pin"]} {t["plaza"]}</li>
        <li>{ICO["ticket"]} {t["gratis"]}</li>
      </ul>
      <div class="botones">
        <a class="boton boton-primario" href="#edicion-30">{t["btn_edicion"]} {ICO["flecha"]}</a>
        <a class="boton boton-borde" href="{RUTAS[lang]["noticias"]}">{t["btn_noticias"]}</a>
      </div>
    </div>
    <figure class="portada-cartel">
      {img("img/carteles/cartel-30", t["alt_cartel30"], [500, 1000], "(max-width:880px) 90vw, 520px", carga="eager", prioridad=True)}
      <div class="sello" aria-hidden="true"><div><strong>30</strong>{t["sello"]}</div></div>
    </figure>
  </div>
</section>

<div class="cinta" aria-hidden="true"><div class="cinta-pista">{ritmos}{ritmos}</div></div>

<section class="seccion" aria-labelledby="titulo-cifras">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-cifras">{t["cifras_h2"]}</h2>
      <p>{t["cifras_p"]}</p>
    </div>
    <ul class="cifras">{cifras}</ul>
  </div>
</section>

<section class="seccion oscuro" id="edicion-30" aria-labelledby="titulo-edicion">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-edicion">{t["ed_h2"]}</h2>
      <p>{t["ed_p"]}</p>
    </div>
    <div class="dias">{dias}</div>
    <figure class="banner-cartel aparece">
      {img("img/carteles/banner-30", t["alt_banner"], [800, 1600], "(max-width:1180px) 100vw, 1180px")}
      <figcaption>{t["banner_pie"]}</figcaption>
    </figure>
  </div>
</section>

<section class="seccion" aria-labelledby="titulo-experiencia">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-experiencia">{t["exp_h2"]}</h2>
      <p>{t["exp_p"]}</p>
    </div>
    <ul class="rasgos">{rasgos}</ul>
  </div>
</section>

<section class="seccion rosa" aria-labelledby="titulo-noticias">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-noticias">{t["act_h2"]}</h2>
      <p>{t["act_p"]}</p>
    </div>
    <div class="noticias">{noticias}</div>
    <div class="ver-todo"><a class="boton boton-vino" href="{RUTAS[lang]["noticias"]}">{t["ver_todas"]} {ICO["flecha"]}</a></div>
  </div>
</section>

<section class="seccion oscuro" id="ediciones" aria-labelledby="titulo-ediciones">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-ediciones">{t["ant_h2"]}</h2>
      <p>{t["ant_p"]}</p>
    </div>
    <ul class="carteles">{galeria}</ul>
    <p class="nota-archivo">{t["nota_archivo"]} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>

<section class="seccion" id="sostenibilidad" aria-labelledby="titulo-sostenibilidad">
  <div class="contenedor">
    <div class="seccion-cabecera aparece">
      {CLAVE}
      <h2 id="titulo-sostenibilidad">{t["sos_h2"]}</h2>
      <p>{t["sos_p"]}</p>
    </div>
    <ul class="ejes">{ejes}</ul>
  </div>
</section>

<section class="seccion rosa" id="teror" aria-labelledby="titulo-teror">
  <div class="contenedor dos-col">
    <figure class="teror-foto aparece">
      {img("img/fotos/teror", t["alt_teror"], [800, 1400], "(max-width:880px) 100vw, 560px")}
    </figure>
    <div class="aparece">
      {CLAVE}
      <h2 id="titulo-teror" style="font-size:clamp(2.6rem,6vw,4.4rem)">{t["teror_h2"]}</h2>
      <p>{t["teror_p"]}</p>
      <p>{t["teror_p2"]}</p>
      <div class="enlaces-turismo">
        <a class="boton boton-vino" href="https://turismo.teror.es/" rel="noopener">{t["turismo_teror"]} {ICO["flecha"]}</a>
        <a class="boton boton-vino" href="https://www.holaislascanarias.com/" rel="noopener">{t["islas"]} {ICO["flecha"]}</a>
      </div>
    </div>
  </div>
</section>

<section class="seccion" id="contacto" aria-labelledby="titulo-contacto">
  <div class="contenedor">
    <div class="contacto-caja aparece">
      <div>
        {CLAVE}
        <h2 id="titulo-contacto">{t["contacto_h2"]}</h2>
        <p>{t["contacto_p"]}</p>
      </div>
      <ul class="contacto-lista">
        <li><a href="mailto:{EMAIL}">{ICO["mail"]}<span><small>{t["c_festival"]}</small>{EMAIL}</span></a></li>
        <li><a href="mailto:{EMAIL_PRENSA}">{ICO["mail"]}<span><small>{t["c_prensa"]}</small>{EMAIL_PRENSA}</span></a></li>
        <li><a href="{INSTAGRAM}" rel="noopener">{ICO["ig"]}<span><small>Instagram</small>@flvteror</span></a></li>
        <li><a href="{FACEBOOK}" rel="noopener">{ICO["fb"]}<span><small>Facebook</small>flvteror</span></a></li>
      </ul>
    </div>
  </div>
</section>

<section class="colaboran" aria-labelledby="titulo-colaboran">
  <div class="contenedor">
    <h2 id="titulo-colaboran">{t["colaboran"]}</h2>
    <ul class="logos">
      <li class="logo-ayto"><a href="https://teror.es/" rel="noopener"><img src="/img/logos/ayuntamiento-teror.webp" alt="Ayuntamiento de Teror" loading="lazy" width="151" height="80"></a></li>
      <li><a href="https://turismodeislascanarias.com/" rel="noopener"><img src="/img/logos/islas-canarias.webp" alt="Islas Canarias, Latitud de vida · Promotur Turismo de Islas Canarias" loading="lazy"></a></li>
      <li><a href="https://cabildo.grancanaria.com/" rel="noopener"><img src="/img/logos/cabildo-gran-canaria.webp" alt="Cabildo de Gran Canaria" loading="lazy"></a></li>
      <li><a href="https://www.aguasdeteror.com/" rel="noopener"><img src="/img/logos/aguas-de-teror.webp" alt="Aguas de Teror" loading="lazy"></a></li>
      <li><a href="https://aperitivossnack.com/" rel="noopener"><img src="/img/logos/aperitivos-snack.webp" alt="Aperitivos Snack" loading="lazy"></a></li>
      <li><a href="https://www.ahembo.com/" rel="noopener"><img src="/img/logos/ahembo.webp" alt="Ahembo" loading="lazy"></a></li>
    </ul>
  </div>
</section>'''
    return pagina(lang, t["titulo"], t["descripcion"], base, cuerpo, alternas, extra_head=extra)


# ---------------------------------------------------------------- noticias
def listado_noticias(lang):
    t = T[lang]
    alternas = {l: RUTAS[l]["noticias"] for l in IDIOMAS}
    tarjetas = "".join(tarjeta_noticia(n, lang) for n in NOTICIAS)
    cuerpo = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <nav class="migas" aria-label="{t["ruta"]}"><a href="{RUTAS[lang]["base"]}">{t["inicio"]}</a> / {t["noticias"]}</nav>
    <h1>{t["noticias"]}</h1>
    <p class="meta">Festival Latino Villa de Teror</p>
  </div>
</section>
<section class="seccion rosa" aria-label="{t["noticias"]}">
  <div class="contenedor"><div class="noticias">{tarjetas}</div></div>
</section>'''
    return pagina(lang, t["noticias_titulo"], t["noticias_desc"], RUTAS[lang]["noticias"], cuerpo, alternas,
                  seccion="noticias")


def noticia(n_es, lang):
    t, n = T[lang], noticia_en(n_es, lang)
    alternas = {l: url_noticia(n_es["slug"], l) for l in IDIOMAS}
    imagen_grande = f'/{n["imagen"]}-{n["anchos"][-1]}.webp'
    ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": n["titulo"], "inLanguage": lang,
          "datePublished": n["fecha"], "image": [DOMINIO + imagen_grande],
          "author": {"@type": "Organization", "name": "Ayuntamiento de Teror"},
          "publisher": {"@type": "Organization", "name": "Ayuntamiento de Teror"}}
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    cuerpo = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <nav class="migas" aria-label="{t["ruta"]}"><a href="{RUTAS[lang]["base"]}">{t["inicio"]}</a> / <a href="{RUTAS[lang]["noticias"]}">{t["noticias"]}</a></nav>
    <p class="meta"><time datetime="{n["fecha"]}">{fecha_larga(n["fecha"], lang)}</time> · {t["prensa_teror"]}</p>
    <h1>{esc(n["titulo"])}</h1>
  </div>
</section>
<article class="articulo">
  <div class="contenedor">
    <figure class="articulo-imagen">{img(n["imagen"], n["imagen_alt"], n["anchos"], "(max-width:760px) 100vw, 760px", carga="eager", prioridad=True)}</figure>
    {n["cuerpo"]}
    <a class="boton boton-vino volver" href="{RUTAS[lang]["noticias"]}">{t["todas"]}</a>
  </div>
</article>'''
    return pagina(lang, f'{n["titulo"]} · Festival Latino Villa de Teror', n["resumen"],
                  url_noticia(n_es["slug"], lang), cuerpo, alternas, seccion="noticias",
                  og_img=imagen_grande, tipo="article", extra_head=extra)


# ---------------------------------------------------------------- legales (solo en español)
TITULAR = '''<table>
<tr><th scope="row">Titular</th><td>Ayuntamiento de Teror</td></tr>
<tr><th scope="row">CIF</th><td>P3502700B</td></tr>
<tr><th scope="row">Domicilio</th><td>Plaza Muro Nuevo, 2 · 35330 Teror (Las Palmas)</td></tr>
<tr><th scope="row">Teléfono</th><td><a href="tel:+34928630075">928 630 075</a></td></tr>
<tr><th scope="row">Email</th><td><a href="mailto:ayuntamiento@teror.es">ayuntamiento@teror.es</a></td></tr>
<tr><th scope="row">Sitio web</th><td>festivallatinoteror.es</td></tr>
</table>'''

AVISO = f'''<h2>1. Datos del titular</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
{TITULAR}
<h2>2. Objeto</h2>
<p>Este sitio web informa sobre el Festival Latino Villa de Teror, organizado por el Ayuntamiento de Teror a través de la Concejalía de Festejos: su programación, sus ediciones y sus noticias.</p>
<h2>3. Condiciones de uso</h2>
<p>El acceso a la web es libre y gratuito. Quien la visita se compromete a hacer un uso adecuado de sus contenidos y a no emplearlos para actividades ilícitas o contrarias a la buena fe.</p>
<h2>4. Propiedad intelectual e industrial</h2>
<p>Los textos, carteles, fotografías, logotipos y diseño de esta web pertenecen al Ayuntamiento de Teror o a terceros que han autorizado su uso. Queda prohibida su reproducción, distribución o transformación sin autorización expresa, salvo para uso personal y privado o para la difusión informativa del festival citando la fuente.</p>
<p>Las marcas y logotipos de las entidades colaboradoras (Gobierno de Canarias, Promotur Turismo de Islas Canarias, Cabildo de Gran Canaria y patrocinadores) pertenecen a sus respectivos titulares.</p>
<h2>5. Responsabilidad</h2>
<p>El Ayuntamiento de Teror procura que la información publicada, incluidas fechas, horarios y artistas, sea correcta y esté actualizada, pero puede haber cambios de programación ajenos a su voluntad. Las versiones en inglés y francés son traducciones informativas; en caso de discrepancia prevalece la versión en español. La web contiene enlaces a sitios de terceros, de cuyos contenidos no se hace responsable.</p>
<h2>6. Protección de datos y cookies</h2>
<p>El tratamiento de datos personales se explica en la <a href="/privacidad.html">política de privacidad</a> y el uso de cookies en la <a href="/cookies.html">política de cookies</a>.</p>
<h2>7. Legislación aplicable</h2>
<p>Estas condiciones se rigen por la legislación española.</p>'''

PRIVACIDAD = f'''<p>Esta política explica cómo se tratan los datos personales que se facilitan a través de esta web, de acuerdo con el Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD).</p>
<h2>1. Responsable del tratamiento</h2>
{TITULAR}
<p>Para cualquier cuestión sobre protección de datos puede consultar también la <a href="https://teror.es/" rel="noopener">política de privacidad del Ayuntamiento de Teror</a>.</p>
<h2>2. Qué datos se tratan</h2>
<p>Esta web no tiene formularios ni registro de usuarios. Solo se tratan los datos que usted envíe por iniciativa propia al escribir un email a las direcciones de contacto: su nombre, su dirección de correo y el contenido del mensaje.</p>
<p>La web no instala cookies de analítica ni de publicidad. Puede utilizarse Cloudflare Web Analytics, que mide visitas de forma agregada sin cookies ni identificadores personales.</p>
<h2>3. Finalidad y base legal</h2>
<p>Los datos se usan únicamente para responder a su consulta. La base legal es el consentimiento que usted presta al escribirnos y, en su caso, el ejercicio de las competencias municipales en materia de cultura y festejos.</p>
<h2>4. Conservación</h2>
<p>Los datos se conservan el tiempo necesario para atender la consulta y, después, durante los plazos que exija la normativa aplicable.</p>
<h2>5. Destinatarios</h2>
<p>No se ceden datos a terceros salvo obligación legal. La web se aloja en Cloudflare, Inc., que actúa como encargado del tratamiento con garantías adecuadas para las transferencias internacionales de datos.</p>
<h2>6. Sus derechos</h2>
<p>Puede ejercer sus derechos de acceso, rectificación, supresión, oposición, limitación del tratamiento y portabilidad escribiendo a <a href="mailto:ayuntamiento@teror.es">ayuntamiento@teror.es</a> o por registro en el Ayuntamiento de Teror. Si considera que sus derechos no se han respetado, puede presentar una reclamación ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es/" rel="noopener">aepd.es</a>).</p>'''

COOKIES = '''<p>Esta web no utiliza cookies propias ni de terceros con fines de analítica, publicidad o seguimiento, por lo que no muestra aviso de cookies.</p>
<h2>Qué puede almacenarse</h2>
<p>Únicamente las cookies técnicas estrictamente necesarias que pueda requerir el servicio de alojamiento (Cloudflare) para la seguridad y el funcionamiento de la web. Estas cookies están exentas de consentimiento según el artículo 22.2 de la LSSI-CE.</p>
<h2>Enlaces externos</h2>
<p>Los enlaces a Instagram, Facebook u otras webs llevan a sitios de terceros con sus propias políticas de cookies.</p>
<h2>Cómo gestionarlas</h2>
<p>Puede borrar o bloquear las cookies desde la configuración de su navegador.</p>'''


def legal(slug, titulo, descripcion, contenido):
    ruta = f"/{slug}.html"
    alternas = {l: ruta for l in IDIOMAS}
    cuerpo = f'''<section class="legal"><div class="contenedor">
<h1>{titulo}</h1>
<p class="actualizado">Última actualización: noviembre de 2026.</p>
{contenido}
</div></section>'''
    return pagina("es", f"{titulo} · Festival Latino Villa de Teror", descripcion, ruta, cuerpo, alternas)


def no_encontrada():
    alternas = {l: RUTAS[l]["base"] for l in IDIOMAS}
    bloques = "".join(
        f'<div lang="{l}" style="margin-bottom:22px"><p class="meta">Error 404</p>'
        f'<h1 style="margin-bottom:.3em">{T[l]["e404_titulo"]}</h1><p>{T[l]["e404_p"]}</p>'
        f'<a class="boton boton-primario" href="{RUTAS[l]["base"]}">{T[l]["e404_volver"]} {ICO["flecha"]}</a></div>'
        for l in IDIOMAS)
    cuerpo = f'<section class="cabecera-pagina" style="min-height:60vh"><div class="contenedor">{bloques}</div></section>'
    return pagina("es", "Página no encontrada · Festival Latino Villa de Teror", "La página que busca no existe.",
                  "/404.html", cuerpo, alternas)


def escribir(ruta, texto):
    p = RAIZ / ruta.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texto, encoding="utf-8")


def main():
    paginas = 0
    urls = []
    for lang in IDIOMAS:
        base, carpeta = RUTAS[lang]["base"], RUTAS[lang]["noticias"]
        escribir(base + "index.html", inicio(lang))
        escribir(carpeta + "index.html", listado_noticias(lang))
        urls += [base, carpeta]
        for n in NOTICIAS:
            escribir(url_noticia(n["slug"], lang), noticia(n, lang))
            urls.append(url_noticia(n["slug"], lang))
        paginas += 2 + len(NOTICIAS)

    escribir("aviso-legal.html", legal("aviso-legal", "Aviso legal",
             "Aviso legal de la web del Festival Latino Villa de Teror: datos del titular, el Ayuntamiento de Teror.", AVISO))
    escribir("privacidad.html", legal("privacidad", "Política de privacidad",
             "Cómo trata el Ayuntamiento de Teror los datos personales en la web del Festival Latino Villa de Teror.", PRIVACIDAD))
    escribir("cookies.html", legal("cookies", "Política de cookies",
             "Uso de cookies en la web del Festival Latino Villa de Teror.", COOKIES))
    escribir("404.html", no_encontrada())
    urls += ["/aviso-legal.html", "/privacidad.html", "/cookies.html"]
    paginas += 4

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{DOMINIO}{u}</loc></url>" for u in urls]
    sm.append("</urlset>")
    escribir("sitemap.xml", "\n".join(sm) + "\n")
    escribir("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n")
    print("Generadas", paginas, "páginas en", ", ".join(IDIOMAS))


if __name__ == "__main__":
    main()
