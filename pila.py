from pathlib import Path
import runpy

runpy.run_path(Path(__file__).parent / "Segunda Unidad" / "pila.py", run_name="__main__")
