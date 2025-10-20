# main.py
import sys
import pathlib
import time
from src.puzzle import EightPuzzle
from src.search_astar import astar
from src.search_ida import ida_star
from src.heuristics import h_manhattan, goal_positions


# --- Agregar src al path para imports ---
ROOT = pathlib.Path(__file__).resolve().parent
SRC_PATH = ROOT / "src"
sys.path.insert(0, str(SRC_PATH))  # Siempre al inicio del path


def run_algorithm(name, algorithm, puzzle, heuristic):
    start_time = time.time()
    result = algorithm(puzzle, heuristic)
    end_time = time.time()
    print(f"\n--- {name} ---")
    if result:
        print(f"Solución encontrada en {result['time']:.3f} segundos")
        print(f"Nodos expandidos: {result['nodes_expanded']}")
        print(f"Costo de la solución: {result['cost']}")
    else:
        print("No se encontró solución")
    cost = result['cost'] if result else None
    nodes = result['nodes_expanded'] if result else 0
    elapsed = end_time - start_time
    return cost, nodes, elapsed


def main():
    initial_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    puzzle = EightPuzzle(initial_state)
    goal_pos = goal_positions(puzzle.goal)
    
    # Función que envuelve h_manhattan para que use goal_pos
    def manhattan_with_goal(state):
        return h_manhattan(state, goal_pos)

    print("Estado inicial:")
    state = puzzle.initial
    print(f"{state[0:3]}\n{state[3:6]}\n{state[6:9]}")

    run_algorithm("A* (Manhattan)", astar, puzzle, manhattan_with_goal)
    run_algorithm("IDA* (Manhattan)", ida_star, puzzle, manhattan_with_goal)


if __name__ == "__main__":
    main()
