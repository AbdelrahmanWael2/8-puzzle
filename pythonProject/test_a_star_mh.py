import unittest
from pythonProject.AstrarSolverManhattan import AStarSolverM
from pythonProject.EightPuzzle import EightPuzzle
from pythonProject import *


class TestAStarSolver(unittest.TestCase):

    def test_without_parents(self):
        # Test without path reconstruction
        initial_state = "867254301"  # Replace with your actual initial state
        solver = AStarSolverM(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Success")
        path_cost, nodes_expanded = values
        self.assertEqual(path_cost, 27)  # No path cost when with_parents is False
        self.assertEqual(nodes_expanded, 8864)  # Replace with the expected number of nodes expanded
        # Add more assertions as needed


if __name__ == '__main__':
    unittest.main()
