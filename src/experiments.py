# ===============================================================
# experiments.py
# ---------------------------------------------------------------
# Ejecuta los algoritmos A* e IDA* sobre distintos estados del 8 puzzle
# y guarda los resultados en un archivo CSV.
# ===============================================================

import csv
from src.puzzle import EightPuzzle
from src.search_astar import astar
from src.search_ida import ida_star
from src.demo_states import TEST_STATES

RESULTS_CSV = 'experiments/results.csv'

def run_all():
    rows = []
    for name, state in TEST_STATES.items():
        problem = EightPuzzle(state)
        if not problem.check_solvability(state):
            print(f"Estado {name} no resoluble, saltando.")
            continue
        print(f'⏳ Ejecutando A* para {name}...')
        r_astar = astar(problem)
        rows.append({
            'case': name,
            'algorithm': 'A*',
            'cost': r_astar['cost'],
            'time_s': r_astar['time'],
            'nodes_expanded': r_astar['nodes_expanded'],
            'max_frontier': r_astar['max_frontier'],
            'ida_iterations': ''
        })
        print(f'⏳ Ejecutando IDA* para {name}...')
        r_ida = ida_star(problem)
        rows.append({
            'case': name,
            'algorithm': 'IDA*',
            'cost': r_ida['cost'] if r_ida else '',
            'time_s': r_ida['time'] if r_ida else '',
            'nodes_expanded': r_ida['nodes_expanded'] if r_ida else '',
            'max_frontier': '',
            'ida_iterations': r_ida['iterations'] if r_ida else ''
        })
    with open(RESULTS_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['case','algorithm','cost','time_s','nodes_expanded','max_frontier','ida_iterations'])
        writer.writeheader()
        writer.writerows(rows)
    print('✅ Experimentos completados. Resultados guardados en', RESULTS_CSV)

if __name__ == '__main__':
    run_all()
