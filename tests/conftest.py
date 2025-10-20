# tests/conftest.py
# Añade la carpeta raíz del proyecto al sys.path para que rom src... funcione en pytest.
import sys
import pathlib

# Ruta al directorio raíz del proyecto (dos niveles arriba de este archivo tests/)
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
