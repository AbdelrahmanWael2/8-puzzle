from solverCommand import SolverCommand
from EightPuzzle import EightPuzzle as ep
import Node


class DFSSolver(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        self.initial_node = Node.Node(node, 0)
        self.with_parents = with_parents

    def execute(self):

        # Initialize the frontier stack, the explored set, and
        # the frontier hashtable for faster neighbour existence checking
        frontier = []
        explored = set()
        frontier_hash = {}
        frontier.append(self.initial_node)
        frontier_hash[self.initial_node.data] = True

        # Initialize the parent array to allow us to print the path
        parents = {self.initial_node.data: self.initial_node.data}

        # Initialize the variable used to maximize the depth
        max_depth = 0

        # Loop until the frontier is empty (should never happen, reason on line 47), or a solution is reached
        while frontier:
            state = frontier.pop()
            # max_depth = max(max_depth, state.depth)
            explored.add(state.data)
            if ep.is_goal(state.data):  # Reached 012345678
                path_cost = ep.path_cost(state)
                nodes_expanded = ep.nodes_expanded(explored)
                path = ep.path_to_goal(state, parents)
                # print(path_cost, nodes_expanded, max_depth, path) -> for debugging
                return "Success", (path_cost, nodes_expanded, max_depth, path)
            # Find possible neighbours
            neighbors = ep.actions(state)
            # neighbors = neighbors[::-1] --> Changed the policy from r - d - l - u to u - l - d - r
            for neighbor in neighbors:  # Loop over the neighbouring states, push them to the stack
                if neighbor.data not in frontier_hash and neighbor.data not in explored:
                    frontier.append(neighbor)
                    frontier_hash[neighbor.data] = True
                    parents[neighbor.data] = state.data
                    max_depth = max(max_depth, neighbor.depth)

        # If the frontier becomes empty, the state then is unsolvable
        # Note: this is unreachable because we already implemented the initial state checking code
        print("Not solvable")
        return "False", (0, 0, 0, [])
    # Update 1: Waiting for the EightPuzzle implementation to complete the missing parts
    # Update 2: Completed the missing parts. The path looks like trash, needs to be reformatted (or not if we use a GUI)
    #           Missing last touches (optimizations and possible modifications). One step away from merging ;)
    # Update 3: Reformatted the outputs, and changed the policy from RDLU to ULDR
    # Update 4: Finalized the code, merging now...
