from abc import ABC
from Node import Node


# the implementation of the interface

def swap_characters(s, index1, index2):
    # Convert the string to a list to make swapping easier
    string_list = list(s)

    # Swap the characters at the given indices
    string_list[index1], string_list[index2] = string_list[index2], string_list[index1]

    # Convert the list back to a string and return it
    return ''.join(string_list)


class EightPuzzle:

    @staticmethod
    def is_goal(state):
        # Define the goal state checking logic
        if state.data == "012345678":
            return True
        return False

    @staticmethod
    def actions(state):
        # Define the actions available for a given state
        pos = state.data.find('0')
        down = pos + 3
        up = pos - 3
        right = pos + 1
        left = pos - 1
        row = pos // 3
        col = pos % 3
        possible_actions = []
        if col < 2:
            possible = state
            swap_characters(possible, pos, right)
            possible_actions.append(Node(possible, state.depth + 1))
        if row < 2:
            possible = state
            swap_characters(possible, pos, down)
            possible_actions.append(Node(possible, state.depth + 1))
        if col > 0:
            possible = state
            swap_characters(possible, pos, left)
            possible_actions.append(Node(possible, state.depth + 1))
        if row > 0:
            possible = state
            swap_characters(possible, pos, up)
            possible_actions.append(Node(possible, state.depth + 1))
        return possible_actions

    @staticmethod
    def path_cost(state):
        return state.depth

    @staticmethod
    def nodes_expanded(expanded_nodes):
        return len(expanded_nodes)

    @staticmethod
    def path_to_goal(state, parents):
        path = []
        while state.data is not None:
            path.append(state.data)
            state.data = parents[state.data]
        path.reverse()
        return path
