class Solution:
    def __init__(self, graph):
        self.graph = graph

    def find_cycle(self):

        n = len(self.graph)
        s = 0
        parents =[None] * n
        visited = [False] * n
        result = []
        stack = [s]
        visited[s] = True
        parents[s] = 0
        result.append(s)
        while stack:
            node = stack.pop()
            for i in self.graph[node]:
                if visited[i] == False:
                    if len(self.graph[i]) == 1 and node == 0:
                        stack.append(i+1)
                        result.append(i+1)
                        parents[i+1] = node
                        visited[i+1] = True
                    else:
                        stack.append(i)
                        result.append(i)
                    parents[i] = node
                    visited[i] = True
                    break
                elif i != parents[node]:
                    result = result[result.index(i):result.index(node)]
                    result.append(node)
                    return result
        
        return []