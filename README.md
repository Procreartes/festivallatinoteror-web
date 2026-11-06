# Festival Latino Villa de Teror — web

Web estática del Festival Latino Villa de Teror (titular: Ayuntamiento de Teror).
Sustituye a la antigua web de Wix. Se publica en Cloudflare (Workers con recursos
estáticos) conectada a este repositorio: cada cambio en `main` se publica solo.

## Idiomas

La web está en español (raíz `/`), inglés (`/en/`) y francés (`/fr/`), con selector de idioma
arriba a la derecha. Los textos de las tres versiones están en `scripts/textos.py`.
Las páginas legales están solo en español (las otras versiones enlazan a ellas).

## Añadir una noticia

1. Abre `scripts/noticias.py`, copia un bloque y cambia los datos (la más reciente, arriba).
   Para las versiones en inglés y francés, añade su traducción en `scripts/noticias_traducidas.py`
   con el mismo `slug` (si no la añades, en esos idiomas se ve en español).
2. Sube la imagen a `img/noticias/` en WebP (por ejemplo `nombre-800.webp`) y pon su ruta en
   `imagen` sin el `-800.webp` final; en `anchos` los tamaños que hayas subido.
3. Ejecuta `python3 scripts/generar.py` y sube los cambios.

Las tres últimas noticias salen solas en la portada.

## Cambiar textos de la portada, legales o el pie

Los textos están en `scripts/textos.py` (en los tres idiomas); los legales, en `scripts/generar.py` (`AVISO`, `PRIVACIDAD`, `COOKIES`).
Después de editar, ejecuta `python3 scripts/generar.py`. No edites los `.html` a mano:
se sobrescriben.

## Imágenes

Las imágenes originales de Wix se trajeron con la acción **Traer imágenes de Wix**
(`.github/workflows/imagenes-wix.yml`), que las descarga y las guarda en WebP en `img/`.
Solo hacía falta una vez; se puede volver a lanzar desde Actions si se pierde algo.

## Qué incluye

Aviso legal, privacidad y cookies · favicon e iconos · `sitemap.xml` y `robots.txt` ·
página 404 · redirecciones de las direcciones antiguas de Wix (`_redirects`) ·
imagen para redes (`og:image`) · textos ALT · imágenes WebP con carga diferida ·
tipografías alojadas en la propia web (sin llamadas a Google) · cabeceras de seguridad
en `_headers` · datos estructurados para Google · contacto solo por email.

Analítica: activar **Cloudflare Web Analytics** desde el panel (no usa cookies).
