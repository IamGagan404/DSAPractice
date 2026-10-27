# Graphs
from collections import deque

def bfs(V,edges):  # V = 5, edges = [ [0, 1], [0, 2], [0, 3], [2, 4] ]
    # prep adj list
    adj = [[] for x in range(V)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    print(adj)
    qu = deque([0])
    visited = [0]*V
    visited[0] = 1
    re = []
    while qu:
        vertex = qu.popleft()
        re.append(vertex)
        neibhors = adj[vertex]
        for n in neibhors:
            if visited[n] == 0:
                visited[n] = 1
                qu.append(n)
    return re

print(bfs( V = 9, edges = [ [0, 1], [0, 3], [1, 2] ]))



def dfs(self, adj):
    # code here
    visited = [0]*len(adj)
    re = []
    def dfs(node):
        neighbors = adj[node]
        re.append(node)
        visited[node] = 1
        for n in neighbors:
            if visited[n] == 0:
                visited[n] = 1
                dfs(n)
    dfs(0)
    return re




