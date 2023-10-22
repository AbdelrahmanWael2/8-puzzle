import re
import time
import Node
from command_factory import CommandFactory


def is_solvable(state):
    # Convert the state string to a list of integers
    state_list = [int(x) for x in re.findall(r'\d', state)]
    # Count the number of inversions
    inversions = 0
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if state_list[i] > state_list[j] != 0 and state_list[i] != 0:
                inversions += 1

    # Check if the number of inversions is even
    if inversions % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # Create an instance of the ConcreteEightPuzzle with an initial state
    initial_state = input("Enter the initial state: ")
    if not is_solvable(initial_state):
        print("The given state is not solvable, try again")
    else:
        command_type = input("1- dfs\n2- bfs\n3- astarManhattan\n4- astarEuclidean\n Enter the command: ")
        with_parents = input("Do you want to print the path to the goal? (y/n): ")
        initial_node = Node.Node(initial_state, 0)
        command = CommandFactory.create_commands(command_type, initial_node, with_parents)
        start_time = time.time()
        command.execute()
        end_time = time.time()
        print("Time taken: ", end_time - start_time)

