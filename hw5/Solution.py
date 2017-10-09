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
        result.append(s)
        while stack:
            print(stack, "\n")
            node = stack.pop()
            print(stack)
            for i in self.graph[node]:
                if visited[i] == False:
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