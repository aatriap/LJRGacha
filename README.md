# Santuario Arcano

App web tipo *gacha* hecha con Flask. Abre sobres cada 5 minutos (máximo 5
acumulados), colecciona cartas con tu propia imagen, una o varias categorías
y descripción en cuatro rarezas, y desbloquea logros que otorgan sobres
extra.

## Características

- **Sobres por tiempo**: se genera un sobre nuevo cada 5 minutos, con un tope
  de 5 acumulados. Cada sobre trae 5 cartas, y podés abrir otro apenas
  termines de revelar el anterior (no hace falta ningún paso extra: las
  cartas ya quedan guardadas en tu colección en el momento en que abrís el
  sobre).
- **Revelado manual**: al abrir un sobre se muestran las 5 cartas boca abajo.
  Al pasar el mouse brillan, y al hacer click se revelan una por una con un
  resplandor y un sonido propios de su rareza (común/rara/épica/legendaria).
- **Cartas con nombre, imagen, categorías y descripción**: cada carta puede
  tener su propia imagen `.png` (ver `static/images/cards/README.md`) y una
  o varias categorías libres. Si todavía no subiste la imagen de una carta,
  se muestran automáticamente las iniciales de su nombre — no hay emojis en
  ninguna parte de la app.
- **72 cartas de ejemplo** repartidas en 4 rarezas: común (30), rara (20),
  épica (14) y legendaria (8) — son un punto de partida editable a mano en
  `cards_data.py`, podés agregar, borrar o reemplazar las que quieras.
- **Colección**: catálogo completo (las cartas que aún no conseguiste se ven
  translúcidas, pero con toda su información visible), filtros por rareza Y
  por categoría, y vista de "mi colección" con tus copias y cantidades.
  Click en cualquier carta abre su ficha grande.
- **Logros**: 14 desafíos (abrir sobres, completar rarezas, llegar al 100%,
  etc.) que se reclaman manualmente y otorgan sobres extra, incluso por
  encima del tope de 5.
- Progreso guardado en una base SQLite local (`gacha.db`). **Cada visitante
  tiene su propia colección y sus propios sobres**, identificado por una
  cookie anónima (un token aleatorio) — no hay login ni se pide ningún dato
  personal.

## Instalación local

```bash
cd gacha_app
python3 -m venv venv          # opcional pero recomendado
source venv/bin/activate      # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar en tu computadora

```bash
python3 app.py
```

Abre `http://127.0.0.1:5000` en tu navegador.

La base de datos `gacha.db` se crea automáticamente la primera vez que
corres la app, en la misma carpeta. Si quieres reiniciar todo el progreso,
simplemente borra ese archivo y vuelve a iniciar la app.

### Probar más rápido (opcional)

Por defecto, un sobre nuevo tarda 5 minutos (300 segundos). Para probar la
app sin esperar tanto:

```bash
PACK_INTERVAL_SECONDS=15 python3 app.py
```

(En Windows / PowerShell: `$env:PACK_INTERVAL_SECONDS=15; python app.py`)

## Estructura del proyecto

```
gacha_app/
├── app.py                    # rutas Flask + lógica del juego (sobres, logros)
├── models.py                  # modelos SQLAlchemy (estado de sobres, colección, logros reclamados)
├── cards_data.py               # lista MANUAL y plana de todas las cartas
├── achievements_data.py        # definición de los 14 logros
├── requirements.txt
├── Procfile                    # comando de arranque para Render/Heroku-like
├── templates/
│   ├── base.html               # layout general: barra superior, navegación, indicador de sobres
│   ├── index.html              # texto y estructura de la página "Santuario" (abrir sobres)
│   ├── collection.html          # texto y estructura de "Colección"
│   └── achievements.html        # texto y estructura de "Logros"
└── static/
    ├── css/style.css           # toda la estética visual: colores, tamaños, animaciones
    ├── images/cards/           # tus imágenes .png de cada carta (ver README ahí)
    ├── audio/                  # tus sonidos .mp3 de revelado por rareza (ver README ahí)
    └── js/
        ├── main.js              # estado global de sobres + cómo se arma el HTML de cada carta
        ├── sanctum.js            # abrir sobres + revelado manual + sonidos
        ├── collection.js         # catálogo / colección personal / filtros / modal
        └── achievements.js       # lista de logros + reclamar recompensa
```

## Cómo personalizar

### Cartas: nombre, imagen, categorías y descripción

Abre `cards_data.py` y edita la lista `CARDS` directamente — es una lista
plana de diccionarios, sin generadores ni funciones automáticas. Cada carta
tiene:

```python
{
    "id": 1,                          # único, no lo repitas
    "name": "Salamandra Joven",       # nombre que se ve en la carta
    "rarity": "comun",                # comun | rara | epica | legendaria
    "categorias": ["Fuego"],          # lista de textos libres, podés poner una o varias
    "image": "001.png",               # archivo dentro de static/images/cards/
    "flavor": "Un ejemplar...",       # la descripción breve de la carta
}
```

`categorias` es siempre una **lista**, aunque sea de un solo elemento — así
una carta puede pertenecer a más de una categoría, por ejemplo
`"categorias": ["Fuego", "Bestia"]`. Estas categorías son las que se usan
para el filtro por categoría en la página de Colección (se generan solas a
partir de lo que pongas ahí, no hay que declararlas en ningún otro lado).

No hay ningún campo de emoji/icono: si una carta todavía no tiene imagen, se
muestran automáticamente las iniciales de su nombre en su lugar.

`name`, la imagen, `rarity · categorias` y `flavor` (la descripción) se
muestran **directamente en la carta**, tanto en el catálogo como al
revelarla. Ya no hace falta abrir la ficha para verlos, aunque la ficha
(al hacer click) sigue mostrando todo en grande.

### Imágenes de las cartas

Coloca el `.png` en `static/images/cards/` con el mismo nombre que el campo
`"image"` de esa carta. Detalles y tamaño recomendado en
`static/images/cards/README.md`.

### Sonidos de revelado (tus propios .mp3)

Coloca tus archivos en `static/audio/` con estos nombres exactos:

```
static/audio/comun.mp3
static/audio/rara.mp3
static/audio/epica.mp3
static/audio/legendaria.mp3
```

Eso es todo — `static/js/sanctum.js` los detecta solo (función
`playRaritySound`). Si falta algún archivo, se usa un sonido sintetizado de
respaldo en su lugar, así que no se rompe nada mientras vas completando los
archivos. Más detalles en `static/audio/README.md`.

### Tamaño de las cartas

El tamaño de las cartas se controla en `static/css/style.css`:

- En la Colección: la clase `.card-grid` (la propiedad
  `grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));` — subí ese
  `230px` si quieres cartas más grandes) y la clase `.card` (`min-height`).
- Al revelar un sobre: la clase `.reveal-slot` (`width` y `height`).
- Cuántas líneas de descripción se muestran antes de cortar el texto:
  `.card-desc` tiene `-webkit-line-clamp: 4` (subí ese número si quieres más
  texto visible en la carta).

### Otras cosas

- **Cambiar probabilidades**: ajusta `RARITY_WEIGHTS` en `cards_data.py`
  (deben sumar 1.0).
- **Agregar logros**: añade un dict a `ACHIEVEMENTS` en `achievements_data.py`
  con un `condition` (`open_packs`, `unique_total`, `unique_rarity` o
  `dupes_total`), su `value` objetivo y el `reward` en sobres.
- **Cambiar el máximo de sobres acumulados o los sobres iniciales**: variables
  `MAX_PACKS` y `STARTER_PACKS` en `app.py`.

## Cómo editar textos y el diseño de la página

No hay un editor visual: todo es código, pero está bien separado por tipo de
cambio:

- **Cambiar un texto** (un título, un párrafo, la etiqueta de un botón) →
  está en los archivos `.html` dentro de `templates/`. Por ejemplo:
  - El nombre del sitio y el menú de navegación → `templates/base.html`.
  - El título "Abre tu sobre del día" y el texto de abajo → `templates/index.html`.
  - Los títulos/textos de la página de Colección → `templates/collection.html`.
  - Los de Logros → `templates/achievements.html`.
  Busca el texto que quieres cambiar (Ctrl+F en el archivo) y reemplázalo
  directamente entre las etiquetas, por ejemplo entre `<h1>...</h1>`.
- **Cambiar colores, tamaños, tipografías, espaciados, animaciones** → todo
  está en `static/css/style.css`. Al principio del archivo hay variables
  como `--gold`, `--bg-deep`, `--legendaria`, etc. — cambiar esas variables
  cambia el color en toda la página de una sola vez.
- **Cambiar el comportamiento** (qué pasa al hacer click, cómo se calculan
  los sobres, etc.) → está en los archivos `.js` dentro de `static/js/` y en
  `app.py` para la lógica del servidor.

Tip: si solo quieres tocar texto y diseño, probablemente nunca necesites
abrir `app.py` ni los `.js` — alcanza con los `.html` y el `.css`.

## Cómo aplicar tus cambios

### Mientras probás en tu computadora

Con la app corriendo (`python3 app.py`):

- Si cambiaste un `.html`, `.css` o `.js`: solo recarga la página en el
  navegador (`Ctrl+R` / `Cmd+R`). Flask sirve esos archivos directamente, no
  hace falta reiniciar nada.
- Si cambiaste `cards_data.py`, `achievements_data.py` o `app.py`: como
  corrés con `debug=True` por defecto, el servidor se reinicia solo apenas
  guardas el archivo (vas a ver "Restarting with watchdog" en la consola).
  Si por algo no se reinicia, paralo (`Ctrl+C`) y volvé a correr
  `python3 app.py`.

### Para que el cambio se vea en la página pública (Render)

1. Guarda tus cambios con git y subilos a GitHub:
   ```bash
   git add .
   git commit -m "Describe brevemente el cambio"
   git push
   ```
2. Si tenés **Auto-Deploy activado** (es la opción por defecto en Render),
   no necesitas hacer nada más: Render detecta el nuevo commit en la rama
   conectada y automáticamente vuelve a instalar dependencias y reiniciar
   la app. Tarda 1-2 minutos. Podés ver el progreso en tu servicio → pestaña
   **Events** o **Logs**.
3. Si el Auto-Deploy está desactivado, entra al dashboard de tu servicio en
   Render y apreta **Manual Deploy** → **Deploy latest commit**.
4. Cuando el deploy termina (estado **Live** en verde), recarga la página
   pública y ya deberías ver los cambios.

Por las dudas: si solo agregaste o cambiaste imágenes/sonidos (archivos
dentro de `static/`), también necesitas que esos archivos estén en el
repositorio (`git add static/images/cards/...`) — Render solo ve lo que está
en GitHub, no lo que tenés en tu computadora.

## Desplegar en Render.com (primera vez)

1. Sube esta carpeta a un repositorio de GitHub (o GitLab).
2. En Render: **New +** → **Web Service** → conecta tu repositorio.
3. Configuración:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT` (ya está en
     el `Procfile`, Render lo debería detectar solo)
4. Click en **Create Web Service**. Render te da una URL pública
   (`https://tu-app.onrender.com`) que cualquiera puede abrir.

### Importante: persistencia de datos (la colección y los sobres)

Por defecto, el disco de un Web Service de Render es **efímero**: cada vez
que se reinicia o se vuelve a desplegar el servicio, se borra el archivo
`gacha.db` y se pierde todo el progreso. Para que la colección persista de
verdad entre reinicios, agrega un **Persistent Disk**:

1. En el dashboard de tu servicio → pestaña **Disks** → **Add Disk**.
2. Ponle un *Mount Path*, por ejemplo `/var/data`.
3. En **Environment** agrega la variable:
   - `DATABASE_PATH` = `/var/data/gacha.db`
4. Vuelve a desplegar. La app va a guardar la base de datos ahí, y va a
   sobrevivir a reinicios y nuevos despliegues.

Render Disks tienen costo (no entran en el plan gratuito); si por ahora no
te importa que el progreso se reinicie cada tanto, podés usar el plan
gratuito sin disco y listo.

### Nota sobre el progreso por visitante

Cada navegador recibe una cookie con un identificador aleatorio (sin datos
personales) la primera vez que visita la página, y esa cookie es lo que
separa una colección de otra. Esto significa que:

- Si la misma persona entra desde el celular y desde la compu, va a tener
  **dos** colecciones distintas (son dos navegadores distintos).
- Si dos personas comparten el mismo navegador/perfil (por ejemplo, la misma
  compu sin perfiles separados), van a ver la **misma** colección, porque
  comparten la misma cookie.
- Si alguien borra las cookies del sitio, pierde el acceso a su colección
  anterior y arranca una nueva.

Si más adelante quisieras que el progreso se pueda recuperar desde cualquier
dispositivo (por ejemplo con un código personal o un login real), avisame y
lo agregamos.

### Nota sobre el modo debug

El modo debug de Flask (recarga automática, página de errores detallada)
solo se activa cuando corres `python3 app.py` directamente. Cuando Render
usa `gunicorn`, ese modo nunca se activa — no necesitas hacer nada extra.
