# tests/test_puzzle.py
# Pruebas unitarias para la clase EightPuzzle (solvabilidad y operadores).

from src.puzzle import EightPuzzle

def test_solvability_goal():
    goal = (1,2,3,4,5,6,7,8,0)
    p = EightPuzzle(goal)
    assert p.check_solvability(goal) is True

def test_actions_result():
    state = (1,2,3,4,5,6,7,0,8)
    p = EightPuzzle(state)
    acts = p.actions(state)
    # hueco en índice 7 → allowed moves: UP, LEFT, RIGHT? (depends); check that result changes
    for a in acts:
        new = p.result(state, a)
        assert isinstance(new, tuple)
        assert len(new) == 9
