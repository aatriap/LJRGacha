# Imágenes de las cartas

Coloca aquí los archivos `.png` de cada carta. El nombre del archivo debe
coincidir exactamente con el campo `"image"` de esa carta en `cards_data.py`.

Por ejemplo, para la carta:

```python
{
    "id": 1,
    "name": "Salamandra Joven",
    ...
    "image": "001.png",
}
```

el archivo debe llamarse `001.png` y estar en esta misma carpeta
(`static/images/cards/001.png`).

## Recomendaciones

- **Formato**: PNG (admite transparencia).
- **Proporción sugerida**: cuadrada o 4:5 (ej. 400x500px). La imagen se recorta
  automáticamente (`object-fit: cover`) para llenar el recuadro de la carta,
  así que evita poner texto importante muy cerca de los bordes.
- **Nombres**: pueden ser lo que quieras (no es obligatorio usar `001.png`,
  `002.png`...). Lo único que importa es que el nombre del archivo y el valor
  de `"image"` en `cards_data.py` sean idénticos.

## Si todavía no tienes la imagen de una carta

No pasa nada: si el archivo no existe o no carga, la carta muestra
automáticamente las iniciales de su nombre (por ejemplo, "SJ" para
"Salamandra Joven") en vez de romperse o quedar en blanco. No hay ningún
emoji ni icono que tengas que asignar a mano — podés ir agregando las
imágenes de a poco y mientras tanto se ve prolijo igual.
