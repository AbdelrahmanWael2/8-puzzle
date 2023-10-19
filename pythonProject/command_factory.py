from AstrarSolverEuclidean import AStarSolverE
from AstrarSolverManhattan import AStarSolverM
from BFSSolver import BFSSolver
from DFSSolver import DFSSolver


class CommandFactory:
    @staticmethod
    def create_commands(command_type, node, with_parents):
        if with_parents == "y":
            with_parents = True
        else:
            with_parents = False
        if command_type == "1":
            return DFSSolver(node, with_parents)
        elif command_type == "2":
            return BFSSolver(node, with_parents)
        elif command_type == "3":
            return AStarSolverM(node, with_parents)
        elif command_type == "4":
            return AStarSolverE(node, with_parents)
