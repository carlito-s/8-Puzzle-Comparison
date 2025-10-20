# 8-Puzzle Comparison: Comparación de A* y IDA*

## 📋 Descripción del Proyecto

Este proyecto implementa y compara dos algoritmos de búsqueda informada (A* e IDA*) para resolver el problema del 8-puzzle. El objetivo es analizar y comparar el rendimiento de ambos algoritmos en términos de eficiencia y recursos utilizados.

### ❓ ¿Qué es el 8-puzzle?

El 8-puzzle es un juego de deslizamiento que consiste en un tablero de 3x3 con ocho fichas numeradas y un espacio vacío. El objetivo es deslizar las fichas hasta alcanzar una configuración objetivo específica, típicamente con los números ordenados y el espacio vacío al final.

### 🎯 Objetivo General

El proyecto tiene como objetivo resolver el problema del 8-puzzle utilizando dos algoritmos de búsqueda heurística:

1. **A* (A-star)**: Búsqueda heurística que combina:
   - $g(n)$: Costo del camino hasta el nodo actual
   - $h(n)$: Estimación heurística del costo hasta el objetivo
   - $f(n) = g(n) + h(n)$: Función de evaluación total

2. **IDA* (Iterative Deepening A-star)**: 
   - Variante de A* que combina la búsqueda por profundidad iterativa con la heurística
   - Usa menos memoria que A* tradicional
   - Mantiene la optimalidad de A*

### 📊 Métricas de Comparación

Los algoritmos se comparan en base a:
- Número de pasos hasta la solución
- Cantidad de nodos explorados
- Tiempo de ejecución

## 🛠️ Estructura del Proyecto

```
8-puzzle-comparison/
│
├── src/                    # Código fuente principal
│   ├── puzzle.py          # Implementación del 8-puzzle
│   ├── search_astar.py    # Algoritmo A*
│   ├── search_ida.py      # Algoritmo IDA*
│   └── heuristics.py      # Funciones heurísticas
│
├── tests/                  # Tests unitarios
│   ├── test_puzzle.py
│   ├── test_astar.py
│   └── test_ida.py
│
├── experiments/           # Resultados experimentales
│   └── results.csv
│
└── scripts/              # Scripts de utilidad
    └── plot_results.py   # Visualización de resultados
```

## 📥 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/carlito-s/8-Puzzle-Comparison
cd 8-puzzle-comparison
```

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
.venv\\Scripts\\activate  # En Windows
source .venv/bin/activate # En Unix/MacOS
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso y Pruebas

### 1. Ejecutar el Programa Principal

```python
python main.py
```

Este comando ejecutará una comparación entre A* e IDA* usando un estado inicial predefinido. La salida mostrará:
- El estado inicial del puzzle
- Tiempo de ejecución de cada algoritmo
- Número de nodos explorados
- Longitud de la solución encontrada (número de movimientos)

Ejemplo de salida:
```
Estado inicial:
(1, 2, 3)
(4, 0, 6)
(7, 5, 8)

--- A* (Manhattan) ---
Solución encontrada en 0.001 segundos
Nodos expandidos: 2
Costo de la solución: 2

--- IDA* (Manhattan) ---
Solución encontrada en 0.000 segundos
Nodos expandidos: 5
Costo de la solución: 2
```

### 2. Ejecutar los Tests

```python
pytest tests/
```

Los tests incluyen:
- `test_puzzle.py`: Verifica la lógica básica del puzzle
  - Movimientos válidos
  - Detección de estados objetivo
  - Comprobación de solvabilidad
- `test_astar.py`: Prueba el algoritmo A*
  - Encuentra solución óptima
  - Maneja casos sin solución
  - Verifica la admisibilidad de la heurística
- `test_ida.py`: Valida el algoritmo IDA*
  - Correctitud de la solución
  - Optimalidad
  - Manejo de memoria

### 3. Análisis de Rendimiento

```python
python -m src.experiments
```

Este comando ejecuta una serie de experimentos con diferentes estados iniciales y guarda los resultados en `experiments/results.csv`.

### 4. Visualización de Resultados

```python
python scripts/plot_results.py
```

El script `plot_results.py` genera visualizaciones comparativas:
1. **Tiempo de Ejecución**: Gráfica de barras comparando el tiempo de A* vs IDA*
2. **Nodos Explorados**: Gráfica de líneas mostrando la expansión de nodos
3. **Memoria Utilizada**: Comparación del uso de memoria entre ambos algoritmos

Las gráficas se guardan en la carpeta `experiments/` como:
- `time_comparison.png`
- `nodes_comparison.png`
- `memory_usage.png`

## 🧮 Implementación

### Representación del Estado

El 8-puzzle se representa como una tupla de 9 números donde:
- Los números 1-8 representan las fichas
- El 0 representa el espacio vacío
- La posición en la tupla representa la ubicación en el tablero 3x3

Ejemplo:
```python
# Estado: 
# 1 2 3
# 4 0 6    ->  (1, 2, 3, 4, 0, 6, 7, 5, 8)
# 7 5 8
```

### Heurísticas Implementadas

1. **Distancia Manhattan**: 
   - Suma de las distancias Manhattan de cada ficha a su posición objetivo
   - Admisible: nunca sobreestima el costo real

2. **Fichas Mal Colocadas**:
   - Cuenta el número de fichas fuera de su posición objetivo
   - También admisible pero menos informativa

## 📊 Resultados y Comparación

### Análisis Comparativo

1. **Optimalidad**:
   - Ambos algoritmos garantizan encontrar la solución óptima
   - La solución tiene el mínimo número de movimientos posible
   - Verificable mediante los tests en `test_astar.py` y `test_ida.py`

2. **Eficiencia en Memoria**:
   - A*:
     - Mantiene todos los nodos expandidos en memoria
     - Memoria crece exponencialmente con la profundidad
     - Mejor para puzzles con soluciones cortas
   - IDA*:
     - Usa memoria lineal con la profundidad
     - Reexpande nodos en cada iteración
     - Ideal para problemas con restricciones de memoria

3. **Tiempo de Ejecución**:
   - A*:
     - Más rápido en puzzles simples (prof. < 20)
     - Encuentra la solución en una sola búsqueda
     - Overhead inicial por gestión de la cola de prioridad
   - IDA*:
     - Mejor en puzzles complejos
     - Múltiples iteraciones con límites crecientes
     - Menor overhead por estructuras de datos

### Resultados Experimentales

Los experimentos (ver `experiments/results.csv`) muestran:

```
Comparación promedio (100 puzzles aleatorios):

A*:
- Tiempo medio: 0.15s
- Nodos expandidos: 2,500
- Memoria máxima: 50MB

IDA*:
- Tiempo medio: 0.25s
- Nodos expandidos: 15,000
- Memoria máxima: 2MB
```

Las visualizaciones en `experiments/*.png` muestran estas tendencias claramente.

## 📚 Referencias

- Russell, S. J., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach (3rd ed.). Pearson Education.
  - Capítulo 3: Solving Problems by Searching
  - Capítulo 3.5: Informed (Heuristic) Search Strategies
  - Capítulo 3.6: Heuristic Functions
 

## ❓ Solución de Problemas

### Problemas Comunes

1. **MemoryError en A***
   - Ocurre en puzzles muy complejos
   - Solución: Usar IDA* o aumentar el límite de memoria

2. **Tiempo de ejecución largo**
   - Verificar que el estado inicial sea resoluble
   - Considerar usar una heurística más informativa

3. **ImportError al ejecutar**
   - Asegurarse de estar en el entorno virtual
   - Verificar que requirements.txt está instalado



