# Guía para usar pam-sistemas en asambleas

## ✅ Antes de la reunión
1. **Designen 1–2 facilitadores** (no necesitan ser técnicos)  
2. **Impriman esta guía + 1 copia del formulario en blanco** ([descargar PDF](../examples/formulario-asamblea.pdf))  
3. **Tengan una netbook/tablet con pam-sistemas instalado** (o usen el modo portable desde USB)

## 🔄 Durante la asamblea (60–90 minutos)

### Paso 1: Mapeo colectivo (30 min)
- Pregunten:  
  - *¿Quiénes/qué cosas hacen posible que esto funcione?* → **Rotores**  
  - *¿Qué circula entre ellos?* → **Tuberías** (dinero, saberes, materiales, trabajo)  
- Anoten en papel afiche o pizarra. Usen las metáforas:  
  > *"¿Quién es la **válvula maestra** sin la que se para todo?"*  
  > *"¿Hay algún **circuito** que se repite? (ej: A da a B, B da a C, C da a A)"*

### Paso 2: Digitalización rápida (15 min)
- Un facilitador pasa los datos a `mi-grupo.yaml` (pueden hacerlo en la misma asamblea).  
- Ejemplo mínimo:  
  ```yaml
  sistema: "Nombre del grupo"
  rotores:
    - nombre: "Persona o cosa"
      tipo: persona/herramienta/espacio
      etiquetas: ["rol1", "rol2"]
  tuberias:
    - desde: "A"
      hacia: "B"
      tipo: "qué circula"
      intensidad: 1-5
