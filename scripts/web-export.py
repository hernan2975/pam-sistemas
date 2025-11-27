#!/usr/bin/env python3
"""
Genera sitio web estático autocontenible (HTML único) para compartir sin internet.
"""
import sys
import json
from pathlib import Path
from jinja2 import Template
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pamsistemas.io.parser import cargar_desde_yaml
from pamsistemas.core.analyzer import analizar_sistema

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ sistema.nombre }} - pam-sistemas</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 0; padding: 1rem; }
        .container { max-width: 800px; margin: 0 auto; }
        header { text-align: center; border-bottom: 3px solid #264653; padding-bottom: 1rem; margin-bottom: 2rem; }
        h1 { color: #264653; }
        .card { background: #f8f9fa; border-radius: 8px; padding: 1rem; margin: 1rem 0; }
        .alert { background: #fff3cd; border-left: 4px solid #ffc107; }
        .danger { background: #f8d7da; border-left: 4px solid #dc3545; }
        .success { background: #d4edda; border-left: 4px solid #28a745; }
        .badge { display: inline-block; background: #e9ecef; padding: 0.25em 0.5em; border-radius: 4px; font-size: 0.85em; }
        footer { margin-top: 2rem; text-align: center; color: #6c757d; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ sistema.nombre }}</h1>
            <p>Informe generado con <strong>pam-sistemas</strong> — La Pampa</p>
        </header>

        <div class="card">
            <h2>📊 Resumen</h2>
            <p>Resiliencia: <strong>{{ resultados.resiliencia * 100 | round }}%</strong></p>
        </div>

        {% if resultados.rotores_criticos %}
        <div class="card danger">
            <h2>⚠️ Válvulas Maestras</h2>
            <ul>
            {% for r in resultados.rotores_criticos %}
                <li>{{ r }}</li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}

        {% if resultados.circuitos %}
        <div class="card">
            <h2>🔁 Circuitos</h2>
            <ul>
            {% for ciclo in resultados.circuitos %}
                <li>{{ ciclo | join(' → ') }}</li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}

        <div class="card">
            <h2>🌀 Rotores</h2>
            <ul>
            {% for r in sistema.rotores %}
                <li><strong>{{ r.nombre }}</strong> <span class="badge">{{ r.tipo }}</span>
                    {% if r.etiquetas %}→ {{ r.etiquetas | join(', ') }}{% endif %}
                </li>
            {% endfor %}
            </ul>
        </div>

        <div class="card">
            <h2>💧 Tuberías</h2>
            <ul>
            {% for t in sistema.tuberias %}
                <li>{{ t.desde }} → {{ t.hacia }} 
                    <span class="badge">{{ t.tipo }}</span> 
                    (intensidad: {{ t.intensidad }}{% if t.condicion %}, {{ t.condicion }}{% endif %})
                </li>
            {% endfor %}
            </ul>
        </div>

        <footer>
            <p>Hecho en La Pampa • pam-sistemas v1.0.0</p>
            <p>Este archivo funciona sin internet — compártelo por WhatsApp o USB.</p>
        </footer>
    </div>
</body>
</html>
"""

def main():
    if len(sys.argv) != 2:
        print("Uso: python web-export.py <archivo.yaml>")
        sys.exit(1)
    
    yaml_path = Path(sys.argv[1])
    if not yaml_path.exists():
        print(f"❌ Archivo no encontrado: {yaml_path}")
        sys.exit(1)
    
    sistema = cargar_desde_yaml(yaml_path)
    resultados = analizar_sistema(sistema)
    
    template = Template(HTML_TEMPLATE)
    html = template.render(sistema=sistema, resultados=resultados)
    
    output = yaml_path.with_suffix(".html")
    output.write_text(html, encoding="utf-8")
    print(f"✅ Sitio generado: {output.absolute()}")

if __name__ == "__main__":
    main()
