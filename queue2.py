from pathlib import Path
import runpy


archivo_queue = Path(__file__).parent / "Segunda Unidad" / "queue2.py"
runpy.run_path(str(archivo_queue), run_name="__main__")