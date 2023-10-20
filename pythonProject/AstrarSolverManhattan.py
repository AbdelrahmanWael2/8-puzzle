from pythonProject import Node
from solverCommand import SolverCommand
import heapq
from EightPuzzle import EightPuzzle as ep

goalState = "012345678"


def mh_heuristic(current_node):
    res = current_node.depth
    state = current_node.data
    for char in state:
        if char != '0':
            current_pos = state.index(char)

            target_pos = goalState.index(char)

            distance = abs(current_pos // 3 - target_pos // 3) + abs(current_pos % 3 - target_pos % 3)
            res += distance

    return res


class AStarSolverM(SolverCommand):
    def __init__(self, node, with_parents):
        self.initial_node = Node.Node(node, with_parents)
        self.with_parents = with_parents

    def execute(self):
        frontiers = [(mh_heuristic(self.initial_node), self.initial_node)]
        heapq.heapify(frontiers)
        explored = set()
        parents = {}
        frontiers_hash = set()
        nodes_expanded = 1
        frontiers_hash.add(self.initial_node.data)
        while frontiers:
            _, state = heapq.heappop(frontiers)
            explored.add(state.data)
            if ep.is_goal(state.data):
                path_cost = ep.path_cost(state)
                if self.with_parents:
                    path = ep.path_to_goal(state, parents)
                    return "Success", (path_cost, nodes_expanded, path)
                else:
                    return "Success", (path_cost, nodes_expanded)
            neighbors = ep.actions(state)

            for neighbor in neighbors:
                if neighbor.data not in explored and neighbor.data not in frontiers_hash:
                    nodes_expanded += 1
                    heapq.heappush(frontiers, (mh_heuristic(neighbor), neighbor))
                    frontiers_hash.add(neighbor.data)
                    if self.with_parents:
                        parents[neighbor] = state.data

        return "Fail"
