from typing import Dict, List, Optional
from .model import Sistema, Rotor, Tuberia

def simular_perturbacion(sistema: Sistema, rotor_a_remover: str) -> Dict:
    """Simula qué pasa si un rotor deja de funcionar."""
    rotores_activos = [r for r in sistema.rotores if r.nombre != rotor_a_remover]
    tuberias_activas = [
        t for t in sistema.tuberias 
        if t.desde != rotor_a_remover and t.hacia != rotor_a_remover
    ]
    
    # Contar flujos interrumpidos
    flujos_perdidos = len(sistema.tuberias) - len(tuberias_activas)
    rotores_aislados = [
        r.nombre for r in rotores_activos
        if not any(t.desde == r.nombre or t.hacia == r.nombre for t in tuberias_activas)
    ]
    
    return {
        "rotor_removido": rotor_a_remover,
        "flujos_interrumpidos": flujos_perdidos,
        "rotores_aislados": rotores_aislados,
        "sistema_operativo": len(tuberias_activas) > 0
    }

def simular_cambio_intensidad(sistema: Sistema, tuberia_idx: int, nueva_intensidad: int) -> Dict:
    """Simula cambio en la intensidad de una tubería."""
    if 0 <= tuberia_idx < len(sistema.tuberias):
        t = sistema.tuberias[tuberia_idx]
        delta = nueva_intensidad - t.intensidad
        return {
            "tuberia": f"{t.desde} → {t.hacia} ({t.tipo})",
            "intensidad_anterior": t.intensidad,
            "intensidad_nueva": nueva_intensidad,
            "cambio": delta,
            "impacto": "aumento" if delta > 0 else "disminución" if delta < 0 else "sin cambio"
        }
    return {"error": "Índice de tubería inválido"}
