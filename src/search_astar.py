# ===============================================================
# search_astar.py
# ---------------------------------------------------------------
# Implementación del algoritmo A* para el problema del 8 puzzle.
# Usa una heurística (por defecto, Manhattan) para estimar el costo.
# ===============================================================

import time
from heapq import heappush, heappop
from typing import Dict
from src.heuristics import h_manhattan, goal_positions
from src.puzzle import EightPuzzle

def astar(problem: EightPuzzle, heuristic_fn=None):
    """
    Implementa el algoritmo A*.
    Retorna un diccionario con estadísticas de la búsqueda.
    """
    start = problem.initial
    goal = problem.goal
    goal_pos = goal_positions(goal)

    if heuristic_fn is None:
        heuristic_fn = lambda s: h_manhattan(s, goal_pos)

    t0 = time.time()
    open_heap = [] # Contiene los nodos pendientes por explorar
    g_score: Dict[tuple,int] = {start: 0}
    f0 = heuristic_fn(start)
    heappush(open_heap, (f0, 0, start))
    came_from: Dict[tuple, tuple] = {}
    closed = set()

    nodes_expanded = 0
    max_frontier = 1

    while open_heap:
        max_frontier = max(max_frontier, len(open_heap))
        f, _, node = heappop(open_heap)
        g = g_score[node]
        if problem.is_goal(node):
            path = [node]
            cur = node
            while cur in came_from:
                cur = came_from[cur]
                path.append(cur)
            path.reverse()
            return {
                'path': path,
                'cost': len(path)-1,
                'time': time.time() - t0,
                'nodes_expanded': nodes_expanded,
                'max_frontier': max_frontier
            }
        if node in closed:
            continue
        closed.add(node)
        nodes_expanded += 1
        for action in problem.actions(node):
            succ = problem.result(node, action)
            tentative_g = g + 1
            if succ in closed and tentative_g >= g_score.get(succ, float('inf')):
                continue
            if tentative_g < g_score.get(succ, float('inf')):
                came_from[succ] = node
                g_score[succ] = tentative_g
                f_succ = tentative_g + heuristic_fn(succ)
                heappush(open_heap, (f_succ, tentative_g, succ))
    return None
