# Festival Latino Villa de Teror — web

Web estática del Festival Latino Villa de Teror (titular: Ayuntamiento de Teror).
Sustituye a la antigua web de Wix. Se publica en Cloudflare (Workers con recursos
estáticos) conectada a este repositorio: cada cambio en `main` se publica solo.

## Añadir una noticia

1. Abre `scripts/noticias.py`, copia un bloque y cambia los datos (la más reciente, arriba).
2. Sube la imagen a `img/noticias/` en WebP (por ejemplo `nombre-800.webp`) y pon su ruta en
   `imagen` sin el `-800.webp` final; en `anchos` los tamaños que hayas subido.
3. Ejecuta `python3 scripts/generar.py` y sube los cambios.

Las tres últimas noticias salen solas en la portada.

## Cambiar textos de la portada, legales o el pie

Todo está en `scripts/generar.py` (funciones `inicio`, `AVISO`, `PRIVACIDAD`, `pie`...).
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
