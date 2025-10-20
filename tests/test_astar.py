# tests/test_astar.py
# Verifica que A* resuelve un caso trivial con coste 1.

from src.puzzle import EightPuzzle
from src.search_astar import astar

def test_astar_one_move():
    state = (1,2,3,4,5,6,7,0,8)  # una sola jugada para resolver
    prob = EightPuzzle(state)
    res = astar(prob)
    assert res is not None
    assert res['cost'] == 1
    assert prob.is_goal(res['path'][-1])
