import time
import Node
from command_factory import CommandFactory

if __name__ == '__main__':
    # Create an instance of the ConcreteEightPuzzle with an initial state
    initial_state = input("Enter the initial state: ")
    command_type = input("1- dfs\n2- bfs\n3- astarManhattan\n4- astarEuclidean\n Enter the command: ")
    with_parents = input("Do you want to print the path to the goal? (y/n): ")
    initial_node = Node.Node(initial_state, 0)
    command = CommandFactory.create_commands(command_type, initial_node, with_parents)
    start_time = time.time()
    command.execute()
    end_time = time.time()
    print("Time taken: ", end_time - start_time)

