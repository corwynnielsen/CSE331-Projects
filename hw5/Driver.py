import sys
from Solution import Solution


def read_file(filename):
    graph = {}
    node = 0
    with open(filename, 'r') as input_file:
        for line in input_file:
            adj_nodes = [int(neighbor) for neighbor in line.split()]
            graph[node] = adj_nodes
            node += 1
    return graph

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the testcase filepath as a command line argument")
    else:
        adj_list = read_file(sys.argv[1])
        sol = Solution(adj_list).find_cycle()
        print("Your Solution:")
        print("============================================================================")
        print(sol)
        print("============================================================================")
