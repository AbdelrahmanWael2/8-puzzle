from AstrarSolverEuclidean import AStarSolverE
from AstrarSolverManhattan import AStarSolverM
from BFSSolver import BFSSolver
from DFSSolver import DFSSolver


class CommandFactory:
    @staticmethod
    def create_commands(command_type, node, with_parents):
        if with_parents == 1:
            with_parents = True
        else:
            with_parents = False
        if command_type == "dfs":
            return DFSSolver(node, with_parents)
        elif command_type == "bfs":
            return BFSSolver(node, with_parents)
        elif command_type == "Manhattan":
            return AStarSolverM(node, with_parents)
        elif command_type == "Euclidean":
            return AStarSolverE(node, with_parents)
