# ===============================================================
# puzzle.py
# ---------------------------------------------------------------
# Define la clase EightPuzzle que representa el problema del 8 puzzle.
# Implementa las funciones básicas: acciones posibles, resultado
# de aplicar una acción, verificación del objetivo y comprobación
# de si un estado es resoluble.
# ===============================================================

from typing import Tuple, List

# Un estado es una tupla de 9 enteros (0 representa el espacio vacío)
State = Tuple[int, ...]

class EightPuzzle:
    def __init__(self, initial: State, goal: State = (1,2,3,4,5,6,7,8,0)):
        """
        Inicializa el problema del 8 puzzle.

        Parámetros:
        - initial: Estado inicial del tablero (tupla de 9 enteros).
        - goal: Estado objetivo, por defecto (1,2,3,4,5,6,7,8,0).
        """
        assert len(initial) == 9
        self.initial = initial
        self.goal = goal

    def find_blank(self, state: State) -> int:
        """Devuelve el índice (posición 0..8) donde se encuentra el hueco (0)."""
        return state.index(0)

    def actions(self, state: State) -> List[str]:
        """
        Devuelve las acciones válidas desde un estado dado.
        Las acciones posibles son: 'UP', 'DOWN', 'LEFT', 'RIGHT'.
        """
        possible = ['UP','DOWN','LEFT','RIGHT']
        blank = self.find_blank(state)
        if blank % 3 == 0:
            possible.remove('LEFT')
        if blank % 3 == 2:
            possible.remove('RIGHT')
        if blank < 3:
            possible.remove('UP')
        if blank > 5:
            possible.remove('DOWN')
        return possible

    def result(self, state: State, action: str) -> State:
        """
        Devuelve el nuevo estado que resulta de aplicar una acción.
        """
        blank = self.find_blank(state)
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        nidx = blank + delta[action]
        l = list(state)
        l[blank], l[nidx] = l[nidx], l[blank]
        return tuple(l)

    def is_goal(self, state: State) -> bool:
        """Comprueba si el estado actual es el estado objetivo."""
        return state == self.goal

    def check_solvability(self, state: State) -> bool:
        """
        Determina si un estado es resoluble calculando el número de inversiones.
        Un estado es resoluble si el número de inversiones es par.
        """
        inversion = 0
        flat = [x for x in state if x != 0]
        for i in range(len(flat)):
            for j in range(i+1, len(flat)):
                if flat[i] > flat[j]:
                    inversion += 1
        return inversion % 2 == 0
