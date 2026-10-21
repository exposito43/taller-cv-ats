# Módulo 3 · Formato: columna única, texto real, PDF etiquetado (15 min)

[← Módulo 2](02-prueba-de-extraccion.md) · [Índice](../README.md) · [Módulo 4 →](04-palabras-clave-y-logros.md)

## 3.1 Las cuatro reglas de formato

| Regla | Por qué | Evidencia |
|---|---|---|
| **Una sola columna**, de arriba abajo, sin tablas de maquetación ni cuadros de texto | Los extractores ordenan el texto por posición; dos columnas mezclan líneas | [E] Workday: el resultado depende del orden de las palabras · [P] |
| **Texto real y seleccionable**, con una fuente estándar (Arial, Helvetica, Times) | Si el texto es una imagen o está en curvas, no hay nada que extraer | [E] Workday: sin imágenes ni estilos basados en imagen |
| **Sin barras, estrellas, iconos ni fotos** | No aportan texto; ocupan espacio; pueden romper la extracción | [E] Workday · [P] |
| **Fechas «Mes Año – Mes Año»** en cada puesto | Permite calcular la duración real de cada experiencia | [P] |

## 3.2 Estructura recomendada

Encabezados con nombres **estándar**, en este orden:

1. **Cabecera:** nombre · titular (el puesto al que aspiras) · contacto en una línea (ciudad, teléfono con prefijo +34, correo, LinkedIn, GitHub).
2. **Resumen profesional:** 3–4 líneas; quién eres y qué has hecho.
3. **Competencias técnicas:** por categorías, con los términos exactos del sector.
4. **Experiencia profesional:** orden cronológico inverso; puesto, empresa, fechas y viñetas con verbo de acción.
5. **Formación:** oficial y reciente primero.
6. **Proyectos:** lo que has construido, en una línea cada uno.

## 3.3 PDF etiquetado: buena práctica, no garantía

- Un **PDF etiquetado** contiene un árbol de estructura con títulos (H1, H2, H3), párrafos y listas, y declara un **idioma**. Lo regula la norma **ISO 14289-1 (PDF/UA)**, que se apoya en la especificación del PDF (**ISO 32000**). [E] → [A1–A3](../bibliografia.md#a-formato-de-documentos-y-accesibilidad)
- Ayuda a la **accesibilidad** (lectores de pantalla) y deja el documento ordenado. [E]
- **No hay fuente pública** de que los ATS usen ese árbol. [H] Por eso la columna única es lo esencial y el etiquetado, un extra.

**Cómo obtenerlo sin programas de pago:**

- **En cualquier editor:** usar los estilos «Título 1», «Título 2»… (no negrita a mano) y fijar el idioma del documento.
- **Microsoft Word:** *Archivo → Guardar como → PDF → Opciones* y dejar marcada la casilla de etiquetas de estructura del documento para accesibilidad. Microsoft recomienda pasar antes el Comprobador de accesibilidad. **No uses «Imprimir a PDF»**: puede perder la información de accesibilidad. [E] → [D2](../bibliografia.md#d-herramientas)
- **LibreOffice:** *Archivo → Exportar como → Exportar como PDF → General* y marcar «PDF etiquetado» o «Accesibilidad universal (PDF/UA)», que activa el etiquetado automáticamente. [E] → [D3](../bibliografia.md#d-herramientas)
- **HTML → PDF:** escribir el CV en HTML semántico (`<h1>`, `<h2>`, `<ul>`, `lang="es"`) y convertirlo con Microsoft Edge o Chrome en modo sin interfaz con la opción `--export-tagged-pdf`. Así se generaron los ejemplos de este taller, y la herramienta del taller confirma que salen etiquetados.
- **Comprobarlo:** con la herramienta del taller o con **PAC**, un verificador PDF/UA gratuito para Windows. [E] → [D1](../bibliografia.md#d-herramientas)

## 3.4 Nombre del archivo

`Puesto_Nombre_Apellido.pdf`, sin tildes ni espacios (por ejemplo `Tecnico_de_Soporte_IT_Alex_Ejemplo.pdf`). Así el reclutador y tú lo identificáis rápido. [P]

## Actividad (5 min)

Convertir en papel el CV de dos columnas del ejemplo en uno de una columna: ¿qué orden darías a las secciones?
