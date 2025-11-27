# pam-sistemas

> *"No se trata de arreglar personas, sino de mejorar cómo se conectan."*  
> — Herramienta libre para mapear, analizar y fortalecer sistemas comunitarios en **La Pampa**.

✅ **Sin internet**  
✅ **Sin registro**  
✅ **Sin tecnicismos**  
✅ **Listo para asambleas, talleres y reuniones barriales**

---

## ¿Para quién es?

- 🤝 **Cooperativas** (agua, energía, conectividad, producción)  
- 🌾 **Huertas y granjas colectivas**  
- 🧵 **Talleres productivos** (tejido, panificación, reparación)  
- 💱 **Redes de trueque o monedas sociales**  
- 📚 **Centros culturales, bibliotecas populares, radios comunitarias**  
- 👩‍🏫 **Escuelas técnicas, grupos de formación popular**

Si en tu grupo alguien dice *"esto depende de una sola persona"* o *"no sabemos por qué se trabó"*, esta herramienta te ayuda a ver el sistema completo.

---

## ¿Qué hace?

1. **Mapea** actores, recursos y flujos (dinero, saberes, insumos, trabajo)  
2. **Detecta automáticamente**:  
   - 🔴 **Válvulas maestras**: puntos únicos de falla (ej: única persona que sabe usar la bomba)  
   - 🔄 **Circuitos**: ciclos sanos (trueque) o tóxicos (sobrecarga)  
   - ⚠️ **Dependencias frágiles**: flujos intensos sin respaldo  
3. **Simula cambios**: ¿qué pasa si X se va? ¿si baja la venta?  
4. **Genera informes imprimibles** (PDF) para discutir en asambleas

Todo con metáforas accesibles: **rotores**, **tuberías**, **tanques**, **válvulas** — nada de *nodos*, *grafos* o *algoritmos*.

---

## Casos reales en La Pampa

| Grupo | Hallazgo | Acción tomada |
|-------|-----------|----------------|
| **Huerta Colectiva — Lonquimay** | 3 personas concentraban el 80% del conocimiento técnico | Diseñaron plan de formación por rotación mensual |
| **Taller Textil — Santa Rosa** | El horno de teñido era una *válvula maestra* sin repuestos | Compraron piezas en consorcio con 2 talleres vecinos |
| **Red de Trueque — Eduardo Castex** | Circuito roto: harina → pan, pero pan no volvía a harina | Reactivaron intercambio con molino local |

---

## Instalación

Solo necesitas **Python 3.10+** (viene en casi todas las netbooks nuevas, y se instala fácil en viejas).

### Opción 1: Instalación normal (recomendada)
```bash
pip install pam-sistemas
```
Opción 2: Sin instalar nada (portable)

git clone https://github.com/tu-usuario/pam-sistemas.git
cd pam-sistemas
python -m venv venv
source venv/bin/activate   # Linux/Mac | venv\Scripts\activate (Windows)
pip install -r requirements.txt

Uso básico (en una asamblea)
1. Creá un archivo mi-grupo.yaml (ver ejemplos abajo)
2. Ejecutá:
```bash
pam-sistemas mi-grupo.yaml --pdf
```
3. Imprimí reports/mi-grupo_informe.pdf en kiosco
4. Discutí los resultados en la próxima reunión
Ejemplo mínimo (mi-grupo.yaml)

sistema: "Panadería Comunitaria - General Pico"
rotores:
  - nombre: "Ana"
    tipo: persona
    etiquetas: ["amasado", "horno", "confianza_alta"]
  - nombre: "Horno a leña"
    tipo: herramienta
    etiquetas: ["mantenimiento_mensual", "capacidad_20kg"]
  - nombre: "Vecinos"
    tipo: grupo
    etiquetas: ["compra_diaria", "pago_efectivo"]

tuberias:
  - desde: "Ana"
    hacia: "Horno a leña"
    tipo: "operación"
    intensidad: 5
  - desde: "Horno a leña"
    hacia: "Vecinos"
    tipo: "pan"
    intensidad: 4
  - desde: "Vecinos"
    hacia: "Ana"
    tipo: "dinero"
    intensidad: 4

Salida de ejemplo (consola)

🔍 Análisis: Panadería Comunitaria - General Pico
📊 Resiliencia: 67%

⚠️  Válvulas maestras (riesgo si fallan):
   • Ana
   • Horno a leña

🔁 Circuitos detectados:
   → Ana → Horno a leña → Vecinos → Ana

✅ Informe generado: reports/mi-grupo_informe.pdf   

El PDF incluye:

Diagrama visual (simple, sin cruces)
Lista de alertas con lenguaje claro
Recomendaciones prácticas (ej: "Buscar segunda persona para operar horno")
Espacio para notas de la asamblea
Personalización
🎨 Cambiar colores/estilo del PDF: editá templates/informe.html
🌐 Generar sitio web estático: python scripts/web-export.py mi-grupo.yaml
🖨️ Versión para imprimir en blanco y negro: python scripts/print-friendly.py mi-grupo.yaml
¿Por qué no usa inteligencia artificial?
Porque los sistemas comunitarios se entienden mejor entre quienes los viven.
Esta herramienta no decide por vos: solo amplifica lo que ya saben en conjunto.

Licencia
MIT — con énfasis en uso comunitario, cooperativo y no comercial.
Puedes usarlo, modificarlo y compartirlo libremente — solo pedimos que, si lo mejorás, lo devuelvas al colectivo.

🌍 Hecho en La Pampa, para La Pampa — pero usable en cualquier lugar donde se teje comunidad.
🐍 Código limpio, sin dependencias pesadas, listo para netbooks de 2015.
