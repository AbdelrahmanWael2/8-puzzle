from solverCommand import SolverCommand
from EightPuzzle import EightPuzzle as ep


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
                print("Reached state: " + str(state.data))
                print("Nodes expanded: " + str(ep.nodes_expanded(explored)))
                if self.with_parents:
                    print("Path to goal: " + str(ep.path_to_goal(state, parents)))
                print("Path cost: " + str(ep.path_cost(state)))
                return True
            neighbors = ep.actions(state)
            # neighbors = neighbors[::-1] --> Changed the policy from r - d - l - u to u - l - d - r
            for neighbor in neighbors:
                if neighbor not in frontier_hash and neighbor.data not in explored:
                    frontier.append(neighbor)
                    frontier_hash[neighbor] = True
                    if self.with_parents:
                        parents[neighbor.data] = state.data
        print("Not solvable")
        return False
        pass
    # Update 1: Waiting for the EightPuzzle implementation to complete the missing parts
    # Update 2: Completed the missing parts. The path looks like trash, needs to be reformatted (or not if we use a GUI)
    #           Missing last touches (optimizations and possible modifications). One step away from merging ;)
    # Update 3: Reformatted the outputs, and changed the policy from RDLU to ULDR
