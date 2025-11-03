# ===============================================================
# search_ida.py
# ---------------------------------------------------------------
# Implementación del algoritmo IDA* (Iterative Deepening A*).
# A diferencia del A*, no usa una cola de prioridad; en su lugar,
# realiza iteraciones de profundidad limitada basadas en el valor f = g + h.
# ===============================================================

import time
from src.heuristics import h_manhattan, goal_positions
from src.puzzle import EightPuzzle

class IDAStats:
    """Clase auxiliar para almacenar estadísticas de ejecución."""
    def __init__(self):
        self.nodes_expanded = 0
        self.iterations = 0
        self.max_depth = 0

def ida_star(problem: EightPuzzle, heuristic_fn=None, max_threshold=10**6):
    """
    Implementa el algoritmo IDA*.
    Retorna un diccionario con las estadísticas y la ruta encontrada.
    """
    start = problem.initial
    goal = problem.goal
    goal_pos = goal_positions(goal)

    if heuristic_fn is None:
        heuristic_fn = lambda s: h_manhattan(s, goal_pos)

    t0 = time.time()
    bound = heuristic_fn(start) # umbral actual de f = g + h
    path = [start]
    stats = IDAStats()

    def search(path, g, bound):
        node = path[-1]
        stats.nodes_expanded += 1
        f = g + heuristic_fn(node)
        if f > bound:
            return f
        if problem.is_goal(node):
            return 'FOUND'
        min_over = float('inf')
        for action in problem.actions(node):
            succ = problem.result(node, action)
            if succ in path:
                continue
            path.append(succ)
            res = search(path, g+1, bound)
            if res == 'FOUND':
                return 'FOUND'
            if res < min_over:
                min_over = res
            stats.max_depth = max(stats.max_depth, len(path))
            path.pop()    
        return min_over

    while True:
        stats.iterations += 1
        t = search(path, 0, bound)
        if t == 'FOUND':
            path_found = path[:]
            return {
                'path': path_found,
                'cost': len(path_found)-1,
                'time': time.time() - t0,
                'nodes_expanded': stats.nodes_expanded,
                'iterations': stats.iterations,
                'max_depth': stats.max_depth
            }
        if t == float('inf') or t > max_threshold:
            return None
        bound = t
