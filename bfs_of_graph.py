from collections import deque
def bfsofGraph(adj,s):
    v = len(adj)
    res = []
    q = deque()
    visited = [False] * v
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

def bfsofGraph(adj, s):
    v = len(adj)
    res = []
    q = deque()
    visited = [False] * v
    q.append(s)
    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res


def bfsofGraph(adj, s):
    v = len(adj)
    res = []
    q = deque()
    visited = [False] * v
    q.append(s)
    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if x not in jvisited[x]:
                visited[x] = True
                q.append(x)
    return res

# Situations where BFS is commonly used
# - Exploring all nodes in layers
# - Finding the mimium number of moves
# is also good for flooding
# marking all adjacents cells

# This are good directions up, down, left, right
#directions = [(-1,0), (1,0), (0, -1), (0,1)]
# we could see this later
