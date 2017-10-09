import queue
from collections import OrderedDict

class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        """
        :return: the list of minimum distances from each node to the start node
        """

        n = len(self.graph)
        visited_nodes = dict.fromkeys(self.graph.keys(), False)
        levels = OrderedDict.fromkeys(list(range(n)), 0)

        q = queue.Queue()

        q.put(self.start_node)
        visited_nodes[self.start_node] = True

        while not q.empty():

            node = q.get()

            for i in self.graph[node]:
                if not visited_nodes[i]:
                    levels[i] += 1 + levels[node]
                    q.put(i)
                    visited_nodes[i] = True

        result = list(levels.values())
        for i, val in enumerate(result):
            if i != self.start_node and val == 0:
                levels[i] = -1

        return list(levels.values())
