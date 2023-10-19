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
        # Missing: define the parent tree
        while frontier:
            state = frontier.pop()
            explored.add(state)
            if ep.is_goal(self, state):
                print("reached state: " + state.data)
                # Missing: print the required outputs (depth, cost, path, ...)
                return True
            neighbors = ep.actions(self, state.data)
            for neighbor in neighbors:
                # Missing: add the state to the parent tree as one of the current state's children
                if neighbor not in frontier_hash and neighbor not in explored:
                    new_state = Node.Node(neighbor, state.depth)
                    frontier.append(new_state)
                    frontier_hash[new_state] = True
        print("Not solvable")
        return False
        pass
    # Update 1: Waiting for the EightPuzzle implementation to complete the missing parts
