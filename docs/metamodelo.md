
# Metamodelo accesible — Lenguaje para no expertos

Este proyecto evita términos técnicos (*nodo*, *arco*, *grafo*). En su lugar, usa metáforas físicas intuitivas:

| Concepto sistémico | Metáfora usada | ¿Por qué? | Ejemplo |
|--------------------|----------------|-----------|---------|
| Entidad (persona, máquina, grupo) | **Rotor** | Gira, actúa, transforma | María, la bomba de agua, el mercado |
| Relación direccional | **Tubería** | Conecta, permite fluir | Dinero de mercado a María, agua de bomba a huerta |
| Intensidad del flujo | **Grosor de la tubería** | Visualmente claro | Intensidad 5 = tubería gruesa |
| Punto único de falla | **Válvula maestra** | Si se cierra, todo se detiene | Única persona que sabe arreglar el molino |
| Ciclo cerrado | **Circuito** | Lo que sale vuelve | Verduras → trueque → insumos → más verduras |
| Recurso almacenado | **Tanque** | Capacidad limitada, puede desbordar/vaciarse | Dinero en caja, stock de semillas |
| Condición de flujo | **Válvula reguladora** | Abre/cierra según contexto | "Solo en verano", "Si hay quórum" |

## Reglas simples para mapear
1. **Todo rotor debe tener al menos una tubería de entrada y una de salida**  
   → Si no, es un *sumidero* (recibe pero no da) o *fuente* (da pero no recibe)  
2. **Intensidad 1–5**:  
   - 1: ocasional  
   - 3: regular  
   - 5: constante/crítico  
3. **Etiquetas**: palabras clave que describen roles o limitaciones (máx. 3–4 por rotor)

> Este lenguaje fue validado en talleres con cooperativas de Lonquimay y Eduardo Castex (2025).
