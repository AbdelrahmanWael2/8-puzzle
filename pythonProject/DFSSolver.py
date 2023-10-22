from solverCommand import SolverCommand
from EightPuzzle import EightPuzzle as ep


class DFSSolver(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        self.initial_node = node
        self.with_parents = with_parents

    def execute(self):

        # Initialize the frontier stack, the explored set, and
        # the frontier hashtable for faster neighbour existence checking
        frontier = []
        explored = set()
        frontier_hash = {}
        frontier.append(self.initial_node)
        frontier_hash[self.initial_node] = True

        # Initialize the parent array to allow us to print the path
        parents = {self.initial_node.data: None}

        # Loop until the frontier is empty (should never happen, reason on line 47), or a solution is reached
        while frontier:
            state = frontier.pop()
            explored.add(state.data)
            if ep.is_goal(state.data):  # Reached 012345678
                print("Reached state: " + str(state.data))
                print("Nodes expanded: " + str(ep.nodes_expanded(explored)))
                if self.with_parents:
                    print("Path to goal: " + str(ep.path_to_goal(state, parents)))
                print("Path cost: " + str(ep.path_cost(state)))
                if self.with_parents:
                    return "success", ep.path_cost(state), ep.nodes_expanded(explored), ep.path_to_goal(state, parents)
                else:
                    return "success", ep.path_cost(state), ep.nodes_expanded(explored)

            neighbors = ep.actions(state)
            # neighbors = neighbors[::-1] --> Changed the policy from r - d - l - u to u - l - d - r
            for neighbor in neighbors:  # Loop over the neighbouring states, push them to the stack
                if neighbor not in frontier_hash and neighbor.data not in explored:
                    frontier.append(neighbor)
                    frontier_hash[neighbor] = True
                    if self.with_parents:
                        parents[neighbor.data] = state.data

        # If the frontier becomes empty, the state then is unsolvable
        # Note: this is unreachable because we already implemented the initial state checking code
        print("Not solvable")
        return "false", 0, 0
    # Update 1: Waiting for the EightPuzzle implementation to complete the missing parts
    # Update 2: Completed the missing parts. The path looks like trash, needs to be reformatted (or not if we use a GUI)
    #           Missing last touches (optimizations and possible modifications). One step away from merging ;)
    # Update 3: Reformatted the outputs, and changed the policy from RDLU to ULDR
