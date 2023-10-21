from solverCommand import SolverCommand
from EightPuzzle import EightPuzzle as ep
import Node


class DFSSolver(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        self.initial_node = node
        self.with_parents = with_parents

    def execute(self):
        # Implement DFS algorithm for solving the puzzle
        frontier = []
        explored = set()
        frontier_hash = {}
        frontier.append(self.initial_node)
        frontier_hash[self.initial_node] = True
        parents = {self.initial_node.data: None}
        # Missing: define the parent tree
        while frontier:
            state = frontier.pop()
            explored.add(state.data)
            if ep.is_goal(state.data):
                print("reached state: " + state.data)
                print(ep.nodes_expanded(explored))
                print(ep.path_to_goal(state, parents))
                print(len(parents))
                print(state.depth)
                return True
            neighbors = ep.actions(state)
            neighbors = neighbors[::-1]
            for neighbor in neighbors:
                if neighbor not in frontier_hash and neighbor.data not in explored:
                    frontier.append(neighbor)
                    frontier_hash[neighbor] = True
                    parents[neighbor.data] = state.data
        print("Not solvable")
        return False
        pass
    # Update 1: Waiting for the EightPuzzle implementation to complete the missing parts
    # Update 2: Completed the missing parts. The path looks like trash, needs to be reformatted (or not if we use a GUI)
    #           Missing last touches (optimizations and possible modifications). One step away from merging ;)
