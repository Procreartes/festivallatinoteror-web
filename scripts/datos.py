"""Datos editables de la web (data/*.json), que se cambian desde el portal (Gestor de webs → Festival Latino).

  noticias.json   [{slug, fecha, titulo, resumen, imagen, imagen_alt, cuerpo}]  (la más reciente primero)
                  «cuerpo» puede ser HTML o texto normal: en texto, cada línea en blanco separa párrafos y
                  una línea que empiece por «## » es un subtítulo.
  carteles.json   [{anio, edicion, imagen, cabezas, noticia}]  archivo de carteles por edición
  proxima.json    [{anio, fechas, aviso}]  si hay fechas, sale una franja arriba en todas las páginas
Las fotos se guardan como <ruta>-<ancho>.webp; los anchos disponibles se detectan solos.
"""
import html
import json
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def _cargar(nombre):
    p = RAIZ / "data" / nombre
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def anchos(ruta, defecto=(800,)):
    ws = sorted(int(m.group(1)) for f in (RAIZ / ruta).parent.glob(pathlib.Path(ruta).name + "-*.webp")
                if (m := re.search(r"-(\d+)\.webp$", f.name)))
    return ws or list(defecto)


def cuerpo_html(t):
    t = (t or "").strip()
    if re.search(r"<(p|h2|ul|div)\b", t):
        return t
    bloques, salida = [b.strip() for b in re.split(r"\n\s*\n", t) if b.strip()], []
    for i, b in enumerate(bloques):
        if b.startswith("## "):
            salida.append(f"<h2>{html.escape(b[3:].strip())}</h2>")
        else:
            clase = ' class="entradilla"' if i == 0 else ""
            salida.append(f"<p{clase}>{html.escape(b).replace(chr(10), '<br>')}</p>")
    return "\n".join(salida)


def noticias():
    ns = []
    for n in _cargar("noticias.json"):
        if not (n.get("slug") and n.get("titulo") and n.get("fecha")):
            continue
        ns.append({**n, "cuerpo": cuerpo_html(n.get("cuerpo")), "imagen_alt": n.get("imagen_alt") or n["titulo"],
                   "anchos": anchos(n["imagen"]) if n.get("imagen") else []})
    return sorted(ns, key=lambda n: n["fecha"], reverse=True)


def carteles():
    cs = [c for c in _cargar("carteles.json") if c.get("anio") and c.get("imagen")]
    return [(c["anio"], c.get("edicion", ""), c["imagen"], anchos(c["imagen"], (600,)), html.escape(c.get("cabezas", "")), c.get("noticia", ""))
            for c in sorted(cs, key=lambda c: str(c["anio"]), reverse=True)]


def proxima():
    p = _cargar("proxima.json")
    return p[0] if p else {}
