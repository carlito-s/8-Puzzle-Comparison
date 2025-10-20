# ===============================================================
# heuristics.py
# ---------------------------------------------------------------
# Contiene funciones heurísticas para el 8 puzzle:
# - h_misplaced: cuenta fichas fuera de lugar.
# - h_manhattan: suma de las distancias Manhattan de cada ficha.
# ===============================================================

from typing import Tuple, Dict

State = Tuple[int, ...]

def goal_positions(goal: State) -> Dict[int, Tuple[int,int]]:
    """Devuelve las posiciones (fila, columna) de cada valor en el estado objetivo."""
    return {val: (i//3, i%3) for i, val in enumerate(goal)}

def h_misplaced(state: State, goal: State) -> int:
    """Heurística: número de fichas fuera de lugar (excepto el 0)."""
    return sum(1 for s,g in zip(state, goal) if s != 0 and s != g)

def h_manhattan(state: State, goal_pos: Dict[int, Tuple[int,int]]) -> int:
    """Heurística: suma de las distancias Manhattan de cada ficha a su posición final."""
    total = 0
    for i, val in enumerate(state):
        if val == 0: continue
        r, c = divmod(i, 3)
        gr, gc = goal_pos[val]
        total += abs(r - gr) + abs(c - gc)
    return total
