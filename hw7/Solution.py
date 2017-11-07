from sys import maxsize
from queue import PriorityQueue
class Solution:
    def __init__(self, start_node, end_node, graph):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node

    def outputPath(self):
        distances = {self.start_node: 0}
        previous = {}
        q = PriorityQueue()
        for i in range(len(self.graph)):
            if i != self.start_node:
                distances[i] = maxsize
            previous[i] = None
            q.put((distances[i], i))

        while not q.empty():
            vertex = (q.get())[1]
            if vertex == self.end_node:
                break

            for i in self.graph[vertex][1:]:
                path = distances[vertex] + self.length(vertex, i)
                if path < distances[i]:
                    distances[i] = path
                    previous[i] = vertex

        return self.shortest_path(previous)

    def length(self, node1, node2):
        node1_weight = self.graph[node1][0]
        node2_weight = self.graph[node2][0]
        return abs(node1_weight-node2_weight)

    def shortest_path(self, previous):
         stack = []
         u = self.end_node
         while u in previous.keys() and previous[u] != None:
             stack.append(u)
             u = previous[u]
             print(u)
         stack.append(u)
         if len(stack) == 1:
             return []
         stack.reverse()
         return stack