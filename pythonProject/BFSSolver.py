from solverCommand import SolverCommand
import EightPuzzle


class BFSSolver(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        initial_node = node
        with_parents = with_parents

    def execute(self):
        # Implement BFS algorithm for solving the puzzle
        pass
