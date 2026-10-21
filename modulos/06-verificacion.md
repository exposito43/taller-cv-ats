# Módulo 6 · Verificación antes de enviar (10 min)

[← Módulo 5](05-etica-y-limites.md) · [Índice](../README.md) · [Módulo 7 →](07-linkedin-y-portales.md)

## 6.1 Pruebas técnicas

| Prueba | Cómo | Resultado esperado |
|---|---|---|
| Texto seleccionable | `Ctrl+A` en el PDF y pegar en el Bloc de notas | Orden coherente, sin símbolos raros |
| Extracción automática | `python herramientas/comprobar_cv.py mi_cv.pdf` | Secciones en el orden del documento |
| PDF etiquetado e idioma | La misma herramienta | «Etiquetado: sí» e idioma `es-ES` |
| Accesibilidad | PAC (gratuito, Windows) → [D1](../bibliografia.md#d-herramientas) | Sin errores graves de PDF/UA |
| Fuentes | Propiedades del PDF → Fuentes | Fuentes estándar incrustadas |
| Ortografía | Corrector + lectura en voz alta | Cero faltas |

## 6.2 Checklist puntuado

Puntúa cada línea con **0** (no), **1** (a medias) o **2** (sí):

- [ ] Una sola columna, sin tablas de maquetación ni cuadros de texto.
- [ ] El texto se selecciona y se pega en orden.
- [ ] PDF etiquetado (títulos, listas) e idioma declarado.
- [ ] Encabezados estándar: «Experiencia profesional», «Competencias técnicas», «Formación».
- [ ] Fechas «Mes Año – Mes Año» en cada puesto, sin solapes.
- [ ] Bloque de competencias con términos exactos y ciertos.
- [ ] Las palabras clave principales aparecen también en la experiencia.
- [ ] Sin fotos, iconos, barras ni porcentajes de nivel.
- [ ] Teléfono con +34 y enlaces (LinkedIn, GitHub) como texto.
- [ ] Viñetas con verbo de acción; cifras solo si son tuyas y justificables.
- [ ] Nada inflado: cada línea se puede defender en una entrevista.
- [ ] Coherente con LinkedIn y los portales (fechas, empresas, cifras).
- [ ] Nombre de archivo claro, sin tildes ni espacios; sin DNI/NIE ni dirección completa.

**Resultado (máximo 26):** 24–26 listo para enviar · 18–23 corregir antes · menos de 18 rehacer.

*La escala es una herramienta de autoevaluación del taller, no un estándar del sector.*
