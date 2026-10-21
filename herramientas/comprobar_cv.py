"""Comprueba un CV en PDF: texto extraíble, orden de secciones, etiquetado PDF e idioma.

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
    raiz = r.trailer["/Root"]
    etiquetado = "/StructTreeRoot" in raiz and bool(raiz.get("/MarkInfo", {}).get("/Marked", False))
    idioma = str(raiz.get("/Lang", "")) or "(no declarado)"
    posiciones = {s: bajo.find(s) for s in SECCIONES}
    resultados = [
        ("Texto extraíble", len(texto.split()) > 50, f"{len(texto.split())} palabras"),
        ("PDF etiquetado", etiquetado, "árbol de estructura y /MarkInfo" if etiquetado else "sin árbol de estructura"),
        ("Idioma declarado", idioma != "(no declarado)", idioma),
        ("Secciones estándar", all(v >= 0 for v in posiciones.values()), ", ".join(f"{k}: {'sí' if v >= 0 else 'no'}" for k, v in posiciones.items())),
        ("Fechas «Mes Año»", bool(re.search(r"\b(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)[a-z]*\.? \d{4}", bajo)), "busca p. ej. «Sep 2024»"),
        ("Páginas", len(r.pages) <= 2, f"{len(r.pages)}"),
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
