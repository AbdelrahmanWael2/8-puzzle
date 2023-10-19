class Node:
    def __init__(self, data, depth):
        self.data = str(data)
        self.depth = depth

    def __lt__(self, other):
        # Define how to compare two Node instances
        return self.depth < other.depth  # Compare based on depth for A* search

    def __hash__(self):
        # Define a hash function for the Node class
        return hash((self.data, self.depth))
