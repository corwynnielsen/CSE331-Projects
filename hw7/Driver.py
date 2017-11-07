import sys
from Solution import Solution


def read_file(filename):
    graph = {}
    node = 0
    s = 0
    e = 0
    with open(filename, 'r') as input_file:
        head = [next(input_file) for x in range(2)]
        s = int(head[0])
        e = int(head[1])
        for line in input_file:
            adj_nodes = [int(neighbor) for neighbor in line.split()]
            graph[node] = adj_nodes
            node += 1
    return (s, e, graph)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the testcase filepath as a command line argument")
    else:
        inp = read_file(sys.argv[1])
        sol = Solution(*inp).outputPath()
        print("Your Solution:")
        print("============================================================================")
        print(sol)
        print("============================================================================")
