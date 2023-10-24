import random
from command_factory import CommandFactory
from main import is_solvable
import time


def generate_unique_strings():
    unique_strings = set()
    while len(unique_strings) < 1000:
        digits = list(range(9))
        random.shuffle(digits)
        unique_string = ''.join(map(str, digits))
        if is_solvable(unique_string):
            unique_strings.add(unique_string)
    return list(unique_strings)


class AVERAGE:
    unique_strings = generate_unique_strings()
    methods = ['dfs', 'bfs', 'Manhattan', 'Euclidean']
    av_time = [0, 0, 0, 0]
    av_expand = [0, 0, 0, 0]
    av_depth = [0, 0, 0, 0]
    count = 1
    for cur_state in unique_strings:
        print(f"solving: {count} / 1000")
        count += 1
        for i in range(4):
            command = CommandFactory.create_commands(methods[i], cur_state, 0)
            start_time = time.time()
            status, results = command.execute()
            end_time = time.time()
            av_time[i] += (end_time - start_time)
            av_expand[i] += results[1]
            av_depth[i] += results[2]
    for i in range(4):
        av_expand[i] /= 1000
        av_depth[i] /= 1000
        av_time[i] = round(av_time[i]/1000, 5)
    print("Average times are:")
    print("DFS, BSF, Manhattan, Euclidean")
    print(av_time)
    print("Average #expanded are:")
    print("DFS, BSF, Manhattan, Euclidean")
    print(av_expand)
    print("Average depth are:")
    print("DFS, BSF, Manhattan, Euclidean")
    print(av_depth)


if __name__ == '__main__':
    AVERAGE()
