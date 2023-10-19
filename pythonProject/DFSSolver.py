from solverCommand import SolverCommand
import EightPuzzle


class DFSSolver(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        initial_node = node
        with_parents = with_parents

    def execute(self):
        # Implement DFS algorithm for solving the puzzle
        pass
