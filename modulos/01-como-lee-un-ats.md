# Módulo 1 · Cómo lee un CV un ATS: mitos y realidad (10 min)

[← Índice](../README.md) · [Módulo 2 →](02-prueba-de-extraccion.md)

## Objetivo

Que cada asistente entienda qué hace un sistema de seguimiento de candidatos (ATS, *Applicant Tracking System*) con su CV y qué no hace, para dejar de optimizar contra un enemigo imaginario.

## 1.1 Un modelo por fases

No existe un único ATS: Workday, Greenhouse, Taleo, InfoJobs o LinkedIn implementan cada uno lo suyo. El esquema siguiente es un **modelo didáctico** que encaja con lo que documentan los propios proveedores [E][P]:

```
Candidatura enviada
  │
  ▼
[0] Formulario ── preguntas eliminatorias (permiso de trabajo, idioma, carnet…)
  │
  ▼
[1] Ingesta ── se extrae la capa de texto del PDF o DOCX
  │   Fallo típico: texto convertido en imagen o en curvas → no hay texto que leer
  ▼
[2] Ordenación del texto ── por posición en la página o por estructura
  │   Fallo típico: dos columnas → líneas de una y otra columna mezcladas
  ▼
[3] Reconocimiento de campos ── contacto, experiencia, formación, competencias
  │   Fallo típico: secciones con nombres creativos («Mi viaje» en lugar de «Experiencia»)
  ▼
[4] Búsqueda y orden ── el reclutador busca por palabras y ordena candidatos;
                         algunos ATS añaden una puntuación de encaje
```

## 1.2 Lo que dicen las fuentes oficiales

- **Workday** documenta en su guía de administrador que el resultado del análisis del CV «puede variar según el formato y el orden de las palabras» y recomienda CV **sin imágenes ni estilos basados en imagen**. También indica que **no rellena automáticamente los campos de Idiomas ni de Competencias (Skills)**. [E] → [Bibliografía B3](../bibliografia.md#b-extracción-de-texto-y-software-de-selección)
- **Greenhouse** explica en su centro de ayuda que un CV puede no importarse bien si el archivo no es de un tipo estándar o contiene caracteres que su analizador no reconoce. [E] → [B4](../bibliografia.md#b-extracción-de-texto-y-software-de-selección)

**Consecuencia práctica:** las palabras clave deben aparecer **también dentro de la experiencia**, en contexto, y no solo en una lista de competencias.

## 1.3 Mito: «el ATS rechaza automáticamente el 75 % de los CV»

- Enhancv señala que esa cifra se repite en artículos y vídeos **sin una sola fuente ni dato que la respalde**. No se ha encontrado el estudio original. [P]
- En una encuesta de Enhancv a **25 reclutadores de EE. UU.** (septiembre–octubre de 2025), solo el **8 %** dijo tener el ATS configurado para rechazar automáticamente por contenido o por puntuación. En cambio, **el 100 % usa las preguntas eliminatorias** (permiso de trabajo, licencia, ubicación) cuando la oferta las incluye. [P] → [C3](../bibliografia.md#c-mercado-y-práctica-de-selección)
- **Precaución:** la muestra es muy pequeña y la publica una empresa que vende plantillas de CV. Sirve para cuestionar el mito, no para dar una cifra nueva.

**Formulación correcta para el taller:** el filtro más usado son las **preguntas eliminatorias** del formulario (según la misma encuesta, cada empresa decide si los fallos van directos a descarte o a revisión humana): respóndelas con la verdad y con cuidado. Después, el reclutador **busca** por palabras y **ordena**. Si tu texto no se extrae bien, no apareces en la búsqueda; si apareces pero no puedes defender lo que pone, te descartas tú en la entrevista.

## 1.4 Lo que no está demostrado

- Que los ATS usen el **árbol de etiquetas** del PDF para leerlo. No hay documentación pública que lo diga. [H] El PDF etiquetado sigue siendo buena práctica (módulo 3), pero la garantía real es la **columna única**.
- Que exista un **umbral universal** (75 %, 80 %…) a partir del cual «pasas». [H] Cada empresa configura su sistema.
- Qué librería usa internamente cada proveedor. Apache Tika (con PDFBox) es una herramienta abierta muy conocida para extraer texto, útil para **reproducir** el proceso, pero **ningún proveedor publica que la use**. [H]

## Actividad (3 min)

Pregunta al grupo: *«¿Qué crees que ve el sistema cuando subes tu CV?»* Anota las respuestas; se contrastan en el módulo 2.
