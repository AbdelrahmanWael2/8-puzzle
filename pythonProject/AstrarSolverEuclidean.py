from pythonProject import Node
from solverCommand import SolverCommand
import heapq
from EightPuzzle import EightPuzzle as ep

goalState = "012345678"


def euclidian(state):
    res = state.depth
    cur_state = state.data
    for letter in cur_state:
        cur_pos = cur_state.index(letter)
        goal_pos = goalState.index(letter)
        if cur_pos != goal_pos:
            cur_pos_x = cur_pos // 3
            cur_pos_y = cur_pos % 3
            goal_pos_x = goal_pos // 3
            goal_pos_y = goal_pos % 3
            res += abs(cur_pos_x - goal_pos_x) + abs(cur_pos_y - goal_pos_y)
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
        while frontiers:
            _, state = heapq.heappop(frontiers)
            explored.add(state.data)
            if ep.is_goal(state.data):
                path_cost = ep.path_cost(state)
                if self.with_parents:
                    path = ep.path_to_goal(state, parents)
                    return "Success", (path_cost, nodes_expanded, path)
                else:
                    return "Success", (path_cost, nodes_expanded, [])
            neighbors = ep.actions(state)

            for neighbor in neighbors:
                if neighbor.data not in explored and neighbor.data not in frontiers_hash:
                    nodes_expanded += 1
                    heapq.heappush(frontiers, (euclidian(neighbor), neighbor))
                    frontiers_hash.add(neighbor.data)
                    if self.with_parents:
                        parents[neighbor.data] = state.data
        return "Fail", (0, 0, [])
