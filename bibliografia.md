# Bibliografía verificada

[← Índice](README.md)

Todas las fuentes se consultaron el **21 de octubre de 2026**. Cada entrada indica qué se usa de ella en el taller y su **nivel de evidencia** ([E] documentación oficial o estándar · [P] testimonio o práctica, no demostrado con datos). Lo que no se pudo confirmar aparece al final, en «Descartado o sin confirmar», para que nadie lo repita como cierto.

## A. Formato de documentos y accesibilidad

| Ref. | Fuente | Qué se usa | Nivel |
|---|---|---|---|
| A1 | ISO 32000-2:2020, *Document management — Portable document format — Part 2: PDF 2.0* (2.ª ed., diciembre de 2020). [iso.org/standard/75839](https://www.iso.org/standard/75839.html) · [Anuncio de la PDF Association](https://www.pdfa.org/iso-32000-22020-is-now-available) | Especificación del formato PDF (de pago) | [E] |
| A2 | ISO 14289-1:2014, *PDF/UA-1*. [iso.org/standard/64599](https://www.iso.org/standard/64599.html) · copia patrocinada por la [PDF Association](https://pdfa.org/resource/iso-14289-pdfua/) | PDF etiquetado, estructura y orden lógico de lectura. Existe también ISO 14289-2:2024 (PDF/UA-2) para PDF 2.0 | [E] |
| A3 | W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, Recomendación del 5 de octubre de 2023 (revisión con erratas del 12 de diciembre de 2024). [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/) · [Anuncio del W3C](https://www.w3.org/news/2023/web-content-accessibility-guidelines-wcag-2-2-is-a-w3c-recommendation) | Semántica de encabezados en el HTML de origen | [E] |

## B. Extracción de texto y software de selección

| Ref. | Fuente | Qué se usa | Nivel |
|---|---|---|---|
| B1 | Apache Software Foundation, *Apache Tika*. [tika.apache.org](https://tika.apache.org/) · [Formatos soportados](https://tika.apache.org/docs/4.1.x/formats.html) | Herramienta abierta de extracción de texto; su analizador de PDF usa Apache PDFBox | [E] |
| B2 | Apache Software Foundation, *Apache PDFBox*. [pdfbox.apache.org](https://pdfbox.apache.org/) | Librería abierta de PDF con extracción de texto | [E] |
| B3 | Workday, *Administrator Guide — Resume Parsing* (Recruiting). [doc.workday.com](https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html) | El resultado varía según el formato y el orden de las palabras; recomienda CV sin imágenes; no rellena automáticamente Idiomas ni Competencias | [E] |
| B4 | Greenhouse, *Why didn't the candidate's resume import correctly?* [support.greenhouse.io](https://support.greenhouse.io/hc/en-us/articles/200721684-Why-didn-t-the-candidate-s-resume-import-correctly) | Fallos de importación por tipo de archivo no estándar o caracteres no reconocidos | [E] |
| B5 | Microsoft Learn, *LinkedIn Talent — Recruiter System Connect*. [learn.microsoft.com](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect) | Integración entre LinkedIn Recruiter y un ATS; no documenta análisis de CV | [E] |
| B6 | pypdf, *Extract Text from a PDF*. [pypdf.readthedocs.io](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) | Librería usada por la herramienta del taller | [E] |

## C. Mercado y práctica de selección

| Ref. | Fuente | Qué se usa | Nivel |
|---|---|---|---|
| C1 | Esade, nota sobre el *Informe InfoJobs–Esade «Estado del mercado laboral en España 2025»* (16.ª edición). [esade.edu](https://www.esade.edu/es/noticias/el-informe-infojobs-esade-estado-del-mercado-laboral-en-espana-2025-confirma-la-demanda-de) | Contexto: 2,5 millones de vacantes publicadas en InfoJobs y 4,2 millones de personas inscritas en 2025. **No se citan cifras del sector TIC**: no se han leído en el informe completo | [E] |
| C2 | PeopleCert, *PeopleCert announces agreement to acquire AXELOS*. [peoplecert.org](https://peoplecert.org/news-and-announcements/peoplecert-announces-agreement-to-acquire-axelos) | ITIL pertenece a PeopleCert desde 2021 (compra de AXELOS) | [E] |
| C3 | Enhancv, *Does the ATS Reject Your Resume? 25 Recruiters Explain What Really Happens*. [enhancv.com](https://enhancv.com/blog/does-ats-reject-resumes/) | 25 entrevistas a reclutadores de EE. UU. (sep–oct 2025): 8 % con rechazo automático por contenido configurado; 100 % usan preguntas eliminatorias cuando existen; la cifra del «75 %» circula sin fuente. Muestra pequeña y autor con interés comercial | [P] |
| C4 | Jobscan, *Resume keyword stuffing*. [jobscan.co](https://www.jobscan.co/blog/resume-keyword-stuffing/) | El relleno de palabras clave se detecta y perjudica | [P] |
| C5 | Built In, *Your AI Resume Hacks Probably Won't Fool Hiring Algorithms*. [builtin.com](https://builtin.com/articles/hidden-ai-prompts-in-resume) | Testimonio de reclutadores sobre el texto oculto en el CV | [P] |

## D. Herramientas

| Ref. | Fuente | Qué se usa | Nivel |
|---|---|---|---|
| D1 | axes4, *PAC — PDF Accessibility Checker*. [support.axes4.com](https://support.axes4.com/hc/en-us/articles/7371921627794) · [Ficha en la PDF Association](https://pdfa.org/product/pac/) | Verificador gratuito de PDF/UA para Windows (protocolo Matterhorn) y comprobaciones WCAG | [E] |
| D2 | Microsoft Support, *Create accessible PDFs*. [support.microsoft.com](https://support.microsoft.com/office/create-accessible-pdfs-064625e0-56ea-4e16-ad71-3aa33bb4b7ed) | Exportar a PDF etiquetado desde Microsoft 365 tras el Comprobador de accesibilidad | [E] |
| D3 | LibreOffice Help, *Universal Accessibility (PDF/UA)* y opciones de exportación a PDF. [help.libreoffice.org](https://help.libreoffice.org/latest/en-US/text/shared/01/ref_pdf_export_universal_accessibility.html) | Exportar a PDF etiquetado o PDF/UA | [E] |

## Descartado o sin confirmar

Afirmaciones frecuentes en otros materiales sobre ATS que **este taller no enseña como ciertas**:

| Afirmación | Motivo |
|---|---|
| «El 75 % de los CV se descartan automáticamente» | No se ha encontrado el estudio original; Enhancv [C3] indica que se repite sin fuente ni datos. El origen que algunas webs le atribuyen (una presentación comercial de 2012) tampoco se ha podido comprobar |
| «Si superas el 75–80 % de coincidencia pasas al reclutador» | No hay fuente: cada empresa configura su sistema |
| «Los ATS leen el árbol de etiquetas (accesibilidad) del PDF» | Ningún proveedor lo documenta |
| «Workday, Taleo y Greenhouse usan Apache Tika o PDFBox» | Ningún proveedor lo publica |
| «LinkedIn Recruiter System Connect analiza CV con procesamiento del lenguaje natural» | Su documentación describe una integración de datos, no un analizador de CV |
| «Los términos de ITIL son la base de los algoritmos de filtrado» | Sin fuente; ITIL es vocabulario que aparece en ofertas |
| Límites de tamaño de archivo de Greenhouse (100 MB / 2,5 MB) | Solo aparecen en webs de terceros |
| WCAG 2.2 adoptada como ISO/IEC 40500:2025 | Solo en una fuente secundaria |

¿Has encontrado una fuente oficial que confirme o desmienta algo de esta lista? Abre una *issue* en el repositorio con el enlace.
