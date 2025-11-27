import os
from pathlib import Path
from jinja2 import Template
from weasyprint import HTML
from ..core.model import Sistema
from ..core.analyzer import analizar_sistema

# Plantilla HTML minimalista, imprimible y accesible
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Informe: {{ sistema.nombre }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2cm; line-height: 1.5; }
        .header { text-align: center; border-bottom: 2px solid #264653; padding-bottom: 10px; }
        .section { margin: 20px 0; }
        .alert { color: #e76f51; font-weight: bold; }
        .ok { color: #2a9d8f; }
        .rotores { background: #f8f9fa; padding: 10px; border-left: 4px solid #264653; }
        .tuberias { background: #f8f9fa; padding: 10px; border-left: 4px solid #e9c46a; }
        .nota { font-size: 0.9em; color: #6c757d; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Informe del Sistema</h1>
        <h2>{{ sistema.nombre }}</h2>
        <p>Generado el {{ fecha }}</p>
    </div>

    <div class="section">
        <h3>📊 Resumen</h3>
        <p>Resiliencia: <strong>{{ resultados.resiliencia * 100 | round }}%</strong></p>
    </div>

    {% if resultados.rotores_criticos %}
    <div class="section alert">
        <h3>⚠️ Válvulas Maestras (riesgo si fallan)</h3>
        <ul>
        {% for r in resultados.rotores_criticos %}
            <li>{{ r }}</li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}

    {% if resultados.circuitos %}
    <div class="section">
        <h3>🔁 Circuitos Detectados</h3>
        <ul>
        {% for ciclo in resultados.circuitos %}
            <li>{{ ciclo | join(' → ') }}</li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}

    <div class="section rotores">
        <h3>🌀 Rotores (personas, herramientas, espacios)</h3>
        <ul>
        {% for r in sistema.rotores %}
            <li><strong>{{ r.nombre }}</strong> — {{ r.tipo }} 
                {% if r.etiquetas %}[{{ r.etiquetas | join(', ') }}]{% endif %}
            </li>
        {% endfor %}
        </ul>
    </div>

    <div class="section tuberias">
        <h3>💧 Tuberías (flujos)</h3>
        <ul>
        {% for t in sistema.tuberias %}
            <li>{{ t.desde }} → {{ t.hacia }} 
                ({{ t.tipo }}, intensidad {{ t.intensidad }}{% if t.condicion %}, {{ t.condicion }}{% endif %})
            </li>
        {% endfor %}
        </ul>
    </div>

    <div class="nota">
        <p><em>Este informe fue generado con pam-sistemas — herramienta libre para fortalecer lo comunitario.</em></p>
        <p>Espacio para notas de la asamblea:</p>
        <div style="border: 1px dashed #ccc; min-height: 80px; margin-top: 10px;"></div>
    </div>
</body>
</html>
"""

def exportar_pdf(sistema: Sistema, resultados: dict, salida: Path):
    """Genera PDF listo para imprimir en kiosco."""
    template = Template(TEMPLATE)
    html_str = template.render(
        sistema=sistema,
        resultados=resultados,
        fecha=datetime.now().strftime("%d/%m/%Y")
    )
    
    os.makedirs(salida.parent, exist_ok=True)
    HTML(string=html_str).write_pdf(salida)
