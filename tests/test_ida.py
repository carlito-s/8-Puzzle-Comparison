# tests/test_ida.py
# Verifica que IDA* resuelve un caso trivial con coste 1.

from src.puzzle import EightPuzzle
from src.search_ida import ida_star

def test_ida_one_move():
    state = (1,2,3,4,5,6,7,0,8)
    prob = EightPuzzle(state)
    res = ida_star(prob)
    assert res is not None
    assert res['cost'] == 1
    assert prob.is_goal(res['path'][-1])
