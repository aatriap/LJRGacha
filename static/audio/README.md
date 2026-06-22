# Sonidos de revelado

Coloca aquí tus archivos `.mp3` con estos nombres EXACTOS (en minúscula, sin
acentos):

```
static/audio/comun.mp3
static/audio/rara.mp3
static/audio/epica.mp3
static/audio/legendaria.mp3
```

Cuando revelas una carta, `static/js/sanctum.js` intenta reproducir el
archivo que corresponde a su rareza. Si el archivo no existe (o el navegador
no puede reproducirlo), se usa automáticamente un sonido sintetizado de
respaldo — no se rompe nada si todavía no subiste todos los `.mp3`.

## Si quieres cambiar el nombre o la lógica

Toda la lógica de sonido está en `static/js/sanctum.js`:

- `playRaritySound(rarity)` es la función que se llama al revelar una carta.
  Ahí se construye la ruta `/static/audio/${rarity}.mp3`.
- `playSynthSound(rarity)` es el sonido de respaldo sintetizado (no usa
  archivos). Las notas que usa cada rareza están en el objeto `RARITY_NOTES`,
  un poco más arriba en el mismo archivo.

Si en algún momento quieres usar nombres de archivo distintos, basta con
cambiar esa línea en `playRaritySound`.

## Recomendaciones

- Formato `.mp3` (es el más compatible en navegadores).
- Sonidos cortos (medio segundo a 2 segundos aprox.) funcionan mejor para
  esta interacción tipo "clic y revela".
- Volumen: el código reproduce el audio al 80% del volumen original del
  archivo, así que normalízalos más o menos parejo entre sí si puedes.
