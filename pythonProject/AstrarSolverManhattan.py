from pythonProject import Node
from solverCommand import SolverCommand
import heapq
from EightPuzzle import EightPuzzle as ep

goalState = "012345678"


def mh_heuristic(current_node):
    distance = 0
    current_node_data = str(current_node.data)
    depth = current_node.depth
    for i in range(9):
        if current_node_data[i] != '0':
            current_row, current_col = divmod(current_node_data.index(str(i)), 3)
            goal_row, goal_col = divmod(goalState.index(str(i)), 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            return distance + depth


class AStarSolverM(SolverCommand):
    def __init__(self, node, with_parents):
        self.initial_node = Node.Node(node, with_parents)
        self.with_parents = with_parents

    def execute(self):
        frontiers = [(mh_heuristic(self.initial_node), self.initial_node)]
        heapq.heapify(frontiers)
        explored = set()
        parents = {}

        while frontiers:
            _, state = heapq.heappop(frontiers)
            explored.add(state)
            if ep.is_goal(state):
                path_cost = ep.path_cost(state)
                nodes_expanded = ep.nodes_expanded(explored)
                if self.with_parents:
                    path = ep.path_to_goal(state, parents)
                    return "Success", (path_cost, nodes_expanded, path)
                else:
                    return "Success", (path_cost, nodes_expanded)
            neighbors = ep.actions(state)
            new_frontiers = []
            for neighbor in neighbors:
                if neighbor not in explored:
                    if neighbor not in [s[1] for s in frontiers]:
                        new_frontiers.append((mh_heuristic(neighbor), neighbor))
                        if self.with_parents:  # Check if path required or not
                            parents[neighbor] = state.data
            frontiers.extend(new_frontiers)
            heapq.heapify(frontiers)
        return "Fail"

