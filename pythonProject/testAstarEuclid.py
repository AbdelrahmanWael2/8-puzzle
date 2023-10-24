import unittest
from pythonProject.AstrarSolverEuclidean import AStarSolverE


class TestAStarSolver(unittest.TestCase):
    def test_without_parents_hard2(self):
        initial_state = "867254301"
        solver = AStarSolverE(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Success")
        path_cost, nodes_expanded, depth, path = values
        self.assertEqual(path_cost, 27)
        self.assertEqual(nodes_expanded, 7684)
        # Add more assertions as needed

    def test_without_parents_easy(self):
        # Test without path reconstruction
        initial_state = "125340678"
        solver = AStarSolverE(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Success")
        path_cost, nodes_expanded, depth, path = values
        self.assertEqual(path_cost, 3)
        self.assertEqual(nodes_expanded, 4)

    def test_without_parents_normal(self):
        initial_state = "142658730"
        solver = AStarSolverE(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Success")
        path_cost, nodes_expanded, depth, path = values
        self.assertEqual(path_cost, 8)
        self.assertEqual(nodes_expanded, 11)

    def test_without_parents_unsolvable(self):
        initial_state = "352417806"
        solver = AStarSolverE(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Fail")

    def test_without_parents_hard(self):
        initial_state = "806547231"
        solver = AStarSolverE(initial_state, with_parents=False)
        result, values = solver.execute()

        self.assertEqual(result, "Success")
        path_cost, nodes_expanded, depth, path = values
        self.assertEqual(path_cost, 31)
        self.assertEqual(nodes_expanded, 39074)


if __name__ == "__main__":
    unittest.main()
