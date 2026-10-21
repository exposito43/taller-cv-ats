# Módulo 2 · Demostración: lo que «ve» la máquina (15 min)

[← Módulo 1](01-como-lee-un-ats.md) · [Índice](../README.md) · [Módulo 3 →](03-formato-del-pdf.md)

## Objetivo

Ver con los propios ojos cómo se transforma un CV en texto plano, que es lo que procesa cualquier sistema de selección.

## Material

En la carpeta [`ejemplos/`](https://github.com/exposito43/taller-cv-ats/tree/main/ejemplos) hay el **mismo candidato ficticio** en dos versiones:

| Archivo | Diseño |
|---|---|
| `cv_ficticio_mal.html` / `.pdf` | Dos columnas, barras de nivel, iconos, fechas solo con años, secciones con nombres creativos |
| `cv_ficticio_bien.html` / `.pdf` | Una columna, encabezados estándar, fechas «Mes Año – Mes Año», PDF etiquetado |

## Demostración en directo (10 min)

1. **Prueba manual.** Abre cada PDF, pulsa `Ctrl+A` (seleccionar todo), `Ctrl+C` y pega en el Bloc de notas. Compara el orden del texto.
2. **Prueba automática.** Ejecuta la herramienta del taller sobre los dos:

   ```bash
   python herramientas/comprobar_cv.py ejemplos/cv_ficticio_mal.pdf
   python herramientas/comprobar_cv.py ejemplos/cv_ficticio_bien.pdf
   ```

   La herramienta usa la librería abierta `pypdf` para extraer el texto, comprobar si el PDF está etiquetado y si declara idioma, y buscar las secciones estándar.
3. **Comenta el resultado** (es lo que sale con los ejemplos de esta carpeta):
   - **Barras y estrellas:** las barras de nivel no aportan ninguna palabra («Windows» con una barra al 90 % se queda en «Windows»), y las estrellas se extraen como símbolos sueltos («★ ★ ★ ☆ ☆»).
   - **Dos columnas:** todo el contenido de la columna lateral (contacto, «superpoderes», idiomas) sale **antes** que la experiencia, separado del puesto al que pertenece.
   - **Secciones creativas:** la herramienta no encuentra «experiencia», «formación» ni «competencias», porque se llaman «Mi viaje» o «Lo que he aprendido».
   - **Fechas:** «2019 – 2022» no dice cuántos meses trabajó la persona.
   - **Etiquetado:** el navegador etiquetó **también** el PDF malo. Estar etiquetado no arregla un mal diseño: es un extra, no la solución (módulo 3).
   - **Cuánto texto útil:** el CV malo tiene 99 palabras extraíbles y el bueno, 297, con la misma información de partida.

## Qué demuestra y qué no

- **Demuestra** que el diseño cambia el texto que se puede extraer. [E] (es el comportamiento documentado de cualquier extractor de PDF)
- **No demuestra** cómo puntúa un ATS concreto: eso no es público. [H]

## Actividad (5 min)

Cada asistente hace la prueba de `Ctrl+A` con su propio CV (en su portátil o móvil) y anota un problema que encuentre.
