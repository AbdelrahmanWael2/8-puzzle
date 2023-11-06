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
        self.initial_node = Node.Node(node, 0)
        self.with_parents = with_parents

    def execute(self):
        frontiers = [(mh_heuristic(self.initial_node), self.initial_node)]
        heapq.heapify(frontiers)
        explored = set()
        parents = {self.initial_node.data: self.initial_node.data}
        costs_map = {self.initial_node.data: self.initial_node.depth}
        frontiers_hash = set()
        # nodes_expanded = 1
        frontiers_hash.add(self.initial_node.data)
        max_depth = 0
        while frontiers:
            _, state = heapq.heappop(frontiers)
            explored.add(state.data)
            # max_depth = max(max_depth, state.depth)
            if ep.is_goal(state.data):
                path_cost = ep.path_cost(state)
                path = ep.path_to_goal(state, parents)
                return "Success", (path_cost, ep.nodes_expanded(explored), max_depth, path)
            neighbors = ep.actions(state)

            for neighbor in neighbors:
                if neighbor.data not in explored and neighbor.data not in frontiers_hash:
                    # nodes_expanded += 1
                    heapq.heappush(frontiers, (mh_heuristic(neighbor), neighbor))
                    frontiers_hash.add(neighbor.data)
                    parents[neighbor.data] = state.data
                    costs_map[neighbor.data] = neighbor.depth
                    max_depth = max(max_depth, neighbor.depth)
                elif neighbor.data not in explored and neighbor.data in frontiers_hash:
                    if neighbor.depth < costs_map[neighbor.data]:
                        heapq.heappush(frontiers, (mh_heuristic(neighbor), neighbor))
                        parents[neighbor.data] = state.data
                        costs_map[neighbor.data] = neighbor.depth
                        max_depth = max(max_depth, neighbor.depth)

        return "Fail", (0, 0, 0, [])
