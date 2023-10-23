class Node:
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth

    def __lt__(self, other):
        # Define how to compare two Node instances
        return self.depth < other.depth  # Compare based on depth for A* search
