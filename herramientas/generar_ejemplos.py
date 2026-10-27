"""Convierte los dos CV ficticios de ejemplos/ a PDF con Microsoft Edge en modo sin interfaz.
La versión correcta se exporta con --export-tagged-pdf. Observado el 21-10-2026: la versión actual de Edge etiqueta también
la incorrecta aunque no se le pase la opción; el taller lo usa para mostrar que el etiquetado no arregla un mal diseño.
Uso (Windows):  python herramientas/generar_ejemplos.py     Licencia MIT (ver LICENSE.md)."""
import subprocess
import tempfile
from pathlib import Path

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
EJ = Path(__file__).resolve().parent.parent / "ejemplos"

# Perfil temporal propio: si Edge ya está abierto con el perfil del usuario, la orden headless no imprime nada.
with tempfile.TemporaryDirectory(prefix="edge_taller_", ignore_cleanup_errors=True) as perfil:
    for nombre, etiquetado in (("cv_ficticio_bien", True), ("cv_ficticio_mal", False)):
        pdf = EJ / f"{nombre}.pdf"
        cmd = [EDGE, f"--user-data-dir={perfil}", "--no-first-run", "--headless=new", "--disable-gpu",
               "--no-pdf-header-footer", f"--print-to-pdf={pdf}"]
        cmd += ["--export-tagged-pdf"] if etiquetado else []
        subprocess.run(cmd + [(EJ / f"{nombre}.html").as_uri()], check=True, timeout=90, capture_output=True)
        print(pdf)
