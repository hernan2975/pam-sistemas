import networkx as nx
from .model import Sistema, Rotor, Tuberia

def analizar_sistema(sistema: Sistema):
    G = nx.DiGraph()
    
    for r in sistema.rotores:
        G.add_node(r.nombre, tipo=r.tipo, etiquetas=r.etiquetas)
    
    for t in sistema.tuberias:
        G.add_edge(t.desde, t.hacia, tipo=t.tipo, peso=t.intensidad)
    
    return {
        "rotores_criticos": [
            n for n in G.nodes 
            if G.in_degree(n) == 0 and G.out_degree(n) > 0  # fuente única
        ],
        "circuitos": list(nx.simple_cycles(G)),
        "dependencias_fragiles": [
            (u, v) for u, v, d in G.edges(data=True)
            if d["peso"] >= 4 and len(list(G.predecessors(v))) == 1
        ],
        "resiliencia": round(1 - (len([n for n in G.nodes if G.degree(n) == 1]) / len(G.nodes)), 2)
    }
