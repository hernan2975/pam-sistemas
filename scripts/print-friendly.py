#!/usr/bin/env python3
"""
Genera versión para imprimir en blanco y negro (ahorra tinta, legible en fotocopias).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pamsistemas.io.parser import cargar_desde_yaml
from pamsistemas.core.analyzer import analizar_sistema
from pamsistemas.io.exporter import TEMPLATE as BASE_TEMPLATE
from jinja2 import Template
from weasyprint import HTML

BWN_TEMPLATE = BASE_TEMPLATE.replace(
    "<style>",
    "<style>\n" +
    "body { color: black; background: white; }\n" +
    ".header { border-bottom: 2px solid black; }\n" +
    ".alert { color: black; font-weight: bold; }\n" +
    ".rotores, .tuberias { border-left: 4px solid black; background: #f0f0f0; }\n" +
    "/* Eliminar colores */\n"
).replace("#264653", "black").replace("#e76f51", "black").replace("#2a9d8f", "black").replace("#e9c46a", "black")

def main():
    if len(sys.argv) != 2:
        print("Uso: python print-friendly.py <archivo.yaml>")
        sys.exit(1)
    
    yaml_path = Path(sys.argv[1])
    sistema = cargar_desde_yaml(yaml_path)
    resultados = analizar_sistema(sistema)
    
    template = Template(BWN_TEMPLATE)
    html_str = template.render(
        sistema=sistema,
        resultados=resultados,
        fecha=__import__("datetime").datetime.now().strftime("%d/%m/%Y")
    )
    
    output = yaml_path.parent / "reports" / f"{yaml_path.stem}_imprimir.pdf"
    output.parent.mkdir(exist_ok=True)
    HTML(string=html_str).write_pdf(output)
    print(f"🖨️  PDF para imprimir: {output.absolute()}")

if __name__ == "__main__":
    main()
