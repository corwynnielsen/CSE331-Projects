from sys import maxsize
import heapq
class Solution:
    def __init__(self, start_node, end_node, graph):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node

    def outputPath(self):
        distances = {self.start_node: 0}
        previous = {}
        q = []
        for i in range(len(self.graph)):
            if i != self.start_node:
                distances[i] = maxsize
            previous[i] = None
            
        heapq.heappush(q, (0, self.start_node))
        while q:
            weight, v = heapq.heappop(q)
            if v == self.end_node:
                break

            for i in self.graph[v][1:]:
                path = distances[v] + self.graph[i][0]
                if path < distances[i]:
                    distances[i] = path
                    previous[i] = v
                    heapq.heappush(q, (distances[i], i))

        return self.shortest_path(previous)

    def shortest_path(self, previous):
         stack = []
         u = self.end_node
         while previous[u] != None:
             stack.append(u)
             u = previous[u]
         stack.append(u)
         if len(stack) == 1:
             return []
         stack.reverse()
         return stack