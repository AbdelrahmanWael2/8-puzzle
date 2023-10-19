from abc import ABC


# the implementation of the interface
class EightPuzzle:

    @staticmethod
    def is_goal(self, state):
        # Define the goal state checking logic
        pass

    @staticmethod
    def actions(self, state):
        # Define the actions available for a given state
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
