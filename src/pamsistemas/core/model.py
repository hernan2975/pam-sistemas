from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Rotor:
    nombre: str
    tipo: str  # persona, herramienta, espacio, recurso
    etiquetas: List[str] = field(default_factory=list)
    capacidad: int = 5  # 1-5

@dataclass
class Tuberia:
    desde: str  # nombre del rotor
    hacia: str
    tipo: str   # agua, dinero, saberes, trabajo
    intensidad: int  # 1-5
    condicion: Optional[str] = None  # "solo_verano", "si_hay_sol"

@dataclass
class Sistema:
    nombre: str
    rotores: List[Rotor] = field(default_factory=list)
    tuberias: List[Tuberia] = field(default_factory=list)
    
    def get_rotor(self, nombre: str) -> Optional[Rotor]:
        return next((r for r in self.rotores if r.nombre == nombre), None)
