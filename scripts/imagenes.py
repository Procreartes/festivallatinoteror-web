#!/usr/bin/env python3
"""Descarga las imágenes originales de la antigua web de Wix y las guarda en
WebP optimizado dentro de img/. Lo ejecuta la acción de GitHub
"Traer imágenes de Wix" (una sola vez); también se puede lanzar a mano:

    pip install pillow && python3 scripts/imagenes.py
"""
import io
import pathlib
import urllib.request

from PIL import Image, ImageOps

RAIZ = pathlib.Path(__file__).resolve().parent.parent
WIX = "https://static.wixstatic.com/media/"

# destino (sin sufijo), id del original en Wix, anchos a generar
FOTOS = [
    ("img/carteles/cartel-30", "0171ea_fbcb6d4519ca43e89741dd71e26d5352~mv2.jpg", [500, 1000]),
    ("img/carteles/banner-30", "0171ea_637770a54a674b0c804ee666f234b88a~mv2.jpg", [800, 1600]),
    ("img/carteles/anuncio-30", "0171ea_583f8d87e3ed492ab8c8e0e6ca564d6e~mv2.jpeg", [800]),
    ("img/carteles/cartel-29", "0171ea_0899bb36525943eb8496f50cc41d91bd~mv2.png", [400, 800]),
    ("img/fotos/plaza-2025", "0171ea_0804131d2df84ea782ec484ab0ad037a~mv2.jpg", [800, 1600]),
    ("img/fotos/teror", "0171ea_e02d9a60137d4f2e85a9c88b1b99ca0d~mv2.jpg", [800, 1400]),
    ("img/fotos/experiencia", "0171ea_5163900d9137463a831dec918c26a8db~mv2.jpg", [800, 1400]),
    ("img/fotos/baile", "0171ea_d567509b12f6401481624ca6b118f50d~mv2.jpeg", [600, 1200]),
    ("img/fotos/agenda", "0171ea_09004d794181438b9874b7ad2c30891a~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-1", "0171ea_edd96f1675aa4725ace33338014f1d78~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-2", "0171ea_d6a38cbfebbf4ec5a662b4508963d868~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-3", "0171ea_c50949a69abc4b92b110145675a5922f~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-4", "0171ea_8deb4faa575646b6a22c61777de01fd1~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-5", "0171ea_bf0d50bf4bc54d75b6cbc674b38b1415~mv2.jpg", [600, 1200]),
    ("img/ediciones/edicion-6", "0171ea_682c99a03f504a8d88c221deac260c4e~mv2.jpg", [600, 1200]),
]

# destino, id, recorte opcional (x0, y0, x1, y1) como en Wix, alto final
LOGOS = [
    ("img/logos/ayuntamiento-teror.webp", "0171ea_b8e0727c9c154996b41c1665315114a5~mv2.png", None, 160),
    ("img/logos/islas-canarias.webp", "0171ea_cb2548d957d54724a691c64e00530817~mv2.png", (1520, 0, 2315, 202), 140),
    ("img/logos/islas-canarias-completo.webp", "0171ea_cb2548d957d54724a691c64e00530817~mv2.png", None, 140),
    ("img/logos/cabildo-gran-canaria.webp", "0171ea_81d1e5a79ab14dbc9e53014e889f1433~mv2.jpg", None, 140),
    ("img/logos/aguas-de-teror.webp", "0171ea_3f3e2bbc571241f4a5fb62ca9c424f0a~mv2.jpg", None, 140),
    ("img/logos/aperitivos-snack.webp", "0171ea_8aa7c08c94c54b1091f8846f06b988c3~mv2.jpg", None, 140),
    ("img/logos/ahembo.webp", "0171ea_29bf72a0152140afa2a28c0b2558ace9~mv2.png", None, 60),
]


def bajar(id_wix):
    req = urllib.request.Request(WIX + id_wix, headers={"User-Agent": "festivallatinoteror-web"})
    with urllib.request.urlopen(req, timeout=60) as r:
        im = Image.open(io.BytesIO(r.read()))
        im.load()
    return ImageOps.exif_transpose(im)


def guardar(im, destino, calidad=80):
    p = RAIZ / destino
    p.parent.mkdir(parents=True, exist_ok=True)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA" if "A" in im.getbands() or im.mode == "P" else "RGB")
    im.save(p, "WEBP", quality=calidad, method=6)
    print(f"  {destino}  {im.size[0]}x{im.size[1]}  {p.stat().st_size // 1024} KB")


def main():
    for destino, id_wix, anchos in FOTOS:
        print(destino)
        im = bajar(id_wix).convert("RGB")
        for w in anchos:
            copia = im.copy()
            if copia.width > w:
                copia = copia.resize((w, round(copia.height * w / copia.width)), Image.LANCZOS)
            guardar(copia, f"{destino}-{w}.webp")

    for destino, id_wix, recorte, alto in LOGOS:
        print(destino)
        im = bajar(id_wix)
        if recorte:
            im = im.crop(recorte)
        if im.height > alto:
            im = im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS)
        guardar(im, destino, calidad=90)

    # Imagen para compartir en redes (1200x630) a partir del banner de la 30.ª edición
    im = bajar("0171ea_637770a54a674b0c804ee666f234b88a~mv2.jpg").convert("RGB")
    og = ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=(0.5, 0.5))
    og.save(RAIZ / "img/og-festival-latino-teror.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print("  img/og-festival-latino-teror.jpg")


if __name__ == "__main__":
    main()
