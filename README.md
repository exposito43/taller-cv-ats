# Taller: CV para filtros ATS en el sector IT

Material abierto para un taller de 90 minutos sobre cómo preparar un currículum que los sistemas de selección (ATS) lean bien y que un reclutador pueda defender en una entrevista.

**Autor:** Yulieser Expósito Herrera · [GitHub](https://github.com/exposito43) · [LinkedIn](https://www.linkedin.com/in/yulieser-exposito)
**Versión:** 1.0 · octubre de 2026 · **Licencia:** texto [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es), código MIT (ver [LICENSE.md](LICENSE.md))

---

## Por qué existe este taller

Este material nace de un proyecto personal llamado **JOB**: un agente que revisa ofertas de empleo IT a diario, calcula el encaje de cada oferta con un CV y las ordena en un panel. Para que ese encaje sirviera de algo, primero hubo que entender cómo se lee un CV por máquina y qué reglas de formato y contenido son realmente útiles.

Durante ese trabajo se comprobó que **mucho consejo que circula sobre los ATS no tiene fuente**: el famoso «75 % de los CV se descartan automáticamente», la idea de que todos los ATS puntúan con un umbral fijo o que «leen» las etiquetas de accesibilidad del PDF. Este taller separa lo verificado de lo que es opinión o mito y lo dice en cada caso.

## Regla del taller: nivel de evidencia

Cada afirmación lleva una marca:

| Marca | Significado |
|---|---|
| **[E]** | Estándar o documentación oficial, con enlace en la [bibliografía](bibliografia.md) |
| **[P]** | Práctica extendida o testimonio de reclutadores; razonable, pero no demostrado con datos |
| **[H]** | Hipótesis o dato sin confirmar: no se enseña como hecho |

## Contenido

| Módulo | Tema | Minutos |
|---|---|---|
| [1](modulos/01-como-lee-un-ats.md) | Cómo lee un CV un ATS: mitos y realidad | 10 |
| [2](modulos/02-prueba-de-extraccion.md) | Demostración: lo que «ve» la máquina | 15 |
| [3](modulos/03-formato-del-pdf.md) | Formato: columna única, texto real, PDF etiquetado | 15 |
| [4](modulos/04-palabras-clave-y-logros.md) | Palabras clave y redacción de logros | 20 |
| [5](modulos/05-etica-y-limites.md) | Ética y límites: lo que no se debe hacer | 10 |
| [6](modulos/06-verificacion.md) | Verificación antes de enviar (checklist puntuado) | 10 |
| [7](modulos/07-linkedin-y-portales.md) | LinkedIn y portales: coherencia de datos | 10 |

Además:

- [Bibliografía verificada](bibliografia.md) con enlaces oficiales y fecha de consulta.
- [Ejemplo ficticio](ejemplos/) de CV en dos versiones (mala y buena) para la demostración del módulo 2.
- [Herramienta](herramientas/comprobar_cv.py) en Python para comprobar un PDF: texto extraíble, orden de lectura, etiquetas e idioma.
- [Guía para el ponente](guia-ponente.md): preparación, tiempos y preguntas frecuentes.

## Cómo usarlo

- **Si vas a impartirlo:** empieza por la [guía para el ponente](guia-ponente.md).
- **Si quieres revisar tu propio CV:** ve directamente al [módulo 6](modulos/06-verificacion.md) y pasa la herramienta:

```bash
pip install pypdf
python herramientas/comprobar_cv.py mi_cv.pdf
```

## Aviso

Este material es orientación general. **Ningún formato garantiza superar un filtro concreto**: cada empresa configura su ATS de forma distinta y la decisión final la toma una persona. El objetivo es que tu CV se lea bien y que todo lo que diga sea cierto.

Los ejemplos usan un candidato **ficticio**; cualquier parecido con una persona real es casual.
