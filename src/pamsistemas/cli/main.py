import click
from pathlib import Path
from ..io.parser import cargar_desde_yaml
from ..core.analyzer import analizar_sistema
from ..io.exporter import exportar_pdf

@click.command()
@click.argument("archivo", type=click.Path(exists=True, path_type=Path))
@click.option("--pdf", is_flag=True, help="Generar informe PDF (listo para imprimir)")
def main(archivo, pdf):
    """pam-sistemas: análisis de sistemas comunitarios — La Pampa"""
    sistema = cargar_desde_yaml(archivo)
    resultados = analizar_sistema(sistema)
    
    print(f"\n🔍 Análisis: {sistema.nombre}")
    print(f"📊 Resiliencia: {resultados['resiliencia'] * 100:.0f}%")
    
    if resultados["rotores_criticos"]:
        print("\n⚠️  Válvulas maestras (riesgo si fallan):")
        for r in resultados["rotores_criticos"]:
            print(f"   • {r}")
    
    if resultados["circuitos"]:
        print("\n🔁 Circuitos detectados:")
        for ciclo in resultados["circuitos"]:
            print(f"   → {' → '.join(ciclo)}")
    
    if pdf:
        salida = Path("reports") / f"{archivo.stem}_informe.pdf"
        salida.parent.mkdir(exist_ok=True)
        exportar_pdf(sistema, resultados, salida)
        print(f"\n✅ Informe generado: {salida}")
