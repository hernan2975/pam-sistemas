import yaml
from pathlib import Path
from ..core.model import Sistema, Rotor, Tuberia

def cargar_desde_yaml(ruta: Path) -> Sistema:
    with open(ruta) as f:
        data = yaml.safe_load(f)
    
    rotores = [Rotor(**r) for r in data.get("rotores", [])]
    tuberias = [Tuberia(**t) for t in data.get("tuberias", [])]
    
    return Sistema(nombre=data["sistema"], rotores=rotores, tuberias=tuberias)
