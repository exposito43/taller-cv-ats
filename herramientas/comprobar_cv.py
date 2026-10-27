"""Comprueba un CV en PDF: texto extraíble, secciones estándar, etiquetado PDF, idioma, fechas y páginas.

Uso:  python herramientas/comprobar_cv.py mi_cv.pdf
Requiere: pip install pypdf
Solo lee el archivo; no lo modifica ni lo envía a ningún sitio. Licencia MIT (ver LICENSE.md).
"""
import re
import sys

from pypdf import PdfReader

SECCIONES = ["experiencia", "formación", "competencias"]


def comprobar(ruta):
    r = PdfReader(ruta)
    texto = "\n".join(p.extract_text() or "" for p in r.pages)
    bajo = texto.lower()
    palabras = len(texto.split())
    paginas = len(r.pages)
    raiz = r.trailer["/Root"]
    etiquetado = "/StructTreeRoot" in raiz and bool(raiz.get("/MarkInfo", {}).get("/Marked", False))
    idioma = str(raiz.get("/Lang", ""))
    presentes = {s: s in bajo for s in SECCIONES}
    resultados = [
        ("Texto extraíble", palabras > 50, f"{palabras} palabras"),
        ("PDF etiquetado", etiquetado, "árbol de estructura y /MarkInfo" if etiquetado else "sin árbol de estructura"),
        ("Idioma declarado", bool(idioma), idioma or "(no declarado)"),
        ("Secciones estándar", all(presentes.values()), ", ".join(f"{k}: {'sí' if v else 'no'}" for k, v in presentes.items())),
        ("Fechas «Mes Año»", bool(re.search(r"\b(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)[a-z]*\.? \d{4}", bajo)), "busca p. ej. «Sep 2024»"),
        ("Páginas", paginas <= 2, f"{paginas}"),
    ]
    print(f"\nArchivo: {ruta}")
    for nombre, ok, detalle in resultados:
        print(f"  {'OK   ' if ok else 'REVISA'} {nombre}: {detalle}")
    print("\nPrimeras líneas tal como las extrae la máquina:")
    for linea in [l for l in texto.splitlines() if l.strip()][:15]:
        print("   |", linea)
    return all(ok for _, ok, _ in resultados)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(0 if comprobar(sys.argv[1]) else 1)
