from solverCommand import SolverCommand
import heapq
from EightPuzzle import EightPuzzle as ep

goalState = "012345678"


def mh_heuristic(current_node):
    distance = 0
    depth = current_node.depth
    for i in range(9):
        if current_node[i] != '0':
            current_row, current_col = divmod(current_node.index(str(i)), 3)
            goal_row, goal_col = divmod(goalState.index(str(i)), 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            return distance + depth


class AStarSolverM(SolverCommand):
    initial_node = None
    with_parents = False

    def __init__(self, node, with_parents):
        self.initial_node = node
        self.with_parents = with_parents

    def execute(self):

        frontiers = [(mh_heuristic(self.initial_node), self.initial_node)]
        heapq.heapify(frontiers)
        explored = set()
        parents = {}

        while frontiers:
            state = heapq.heappop(frontiers)
            explored.add(state[1])
            if ep.is_goal(state[1]):
                path_cost = ep.path_cost(state[1])
                nodes_expanded = ep.nodes_expanded(explored)
                if self.with_parents:
                    path = ep.path_to_goal(state[1], parents)
                    return "Success", (path_cost, nodes_expanded, path)
                else:
                    return "Success", (path_cost, nodes_expanded)
            neighbours = ep.actions(state[1])
            for neighbor in neighbours:
                if neighbor not in explored:
                    if neighbor not in [s[1] for s in frontiers]:
                        heapq.heappush(frontiers, (mh_heuristic(neighbor), neighbor))
                        if self.with_parents:  # Check if path required or not
                            parents[neighbor] = state[1].data
                    else:
                        frontiers = [(h, s) if s != neighbor else (min(h, mh_heuristic(neighbor)), neighbor) for h, s in
                                     frontiers]
                        heapq.heapify(frontiers)
        return "Fail"
