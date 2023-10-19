from abc import ABC


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
    def is_goal(self, state):
        # Define the goal state checking logic
        if state == "012345678":
            return True
        return False
        pass

    @staticmethod
    def actions(self, state):
        # Define the actions available for a given state
        pos = state.find('0')
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
            possible_actions.append(possible)
        if row < 2:
            possible = state
            swap_characters(possible, pos, down)
            possible_actions.append(possible)
        if col > 0:
            possible = state
            swap_characters(possible, pos, left)
            possible_actions.append(possible)
        if row > 0:
            possible = state
            swap_characters(possible, pos, up)
            possible_actions.append(possible)
        return possible_actions
        pass

    @staticmethod
    def path_cost(self, state):
        pass

    @staticmethod
    def nodes_expanded(self):
        pass

    @staticmethod
    def path_to_goal(self, state, parents):
        pass
