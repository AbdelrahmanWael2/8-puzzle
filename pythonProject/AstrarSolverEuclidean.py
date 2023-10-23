from pythonProject import Node
from solverCommand import SolverCommand
import heapq
from EightPuzzle import EightPuzzle as ep
import math

goalState = "012345678"


def euclidian(current_node):
    res = current_node.depth
    state = current_node.data
    for char in state:
        if char != '0':
            current_pos = state.index(char)
            target_pos = goalState.index(char)
            distance = math.sqrt(abs(current_pos // 3 - target_pos // 3)**2 + abs(current_pos % 3 - target_pos % 3)**2)
            res += distance
    return res


class AStarSolverE(SolverCommand):
    def __init__(self, node, with_parents):
        self.initial_node = Node.Node(node, with_parents)
        self.with_parents = with_parents

    def execute(self):
        frontiers = [(euclidian(self.initial_node), self.initial_node)]
        heapq.heapify(frontiers)
        explored = set()
        parents = {self.initial_node.data: self.initial_node.data}
        frontiers_hash = set()
        nodes_expanded = 1
        frontiers_hash.add(self.initial_node.data)
        max_depth = 0
        while frontiers:
            _, state = heapq.heappop(frontiers)
            explored.add(state.data)
            max_depth = max(max_depth, state.depth)
            if ep.is_goal(state.data):
                path_cost = ep.path_cost(state)
                path = ep.path_to_goal(state, parents)
                return "Success", (path_cost, nodes_expanded, max_depth, path)
            neighbors = ep.actions(state)

            for neighbor in neighbors:
                if neighbor.data not in explored and neighbor.data not in frontiers_hash:
                    nodes_expanded += 1
                    heapq.heappush(frontiers, (euclidian(neighbor), neighbor))
                    frontiers_hash.add(neighbor.data)
                    parents[neighbor.data] = state.data
        return "Fail", (0, 0, 0, [])
