def solution(entrances, exits, path):
    start = len(path)
    end = len(path) + 1
    path.extend(
        [[float('inf') if n in entrances else 0
          for n in range(len(path))],
         [0] * len(path)])
    for n, y in enumerate(path):
        y.extend([0, float('inf') if n in exits else 0])
    parent = {}
    maxflow = 0
    while bfs(start, end, path, parent):
        flow = float('inf')
        e = end
        while e != start:
            flow = min(flow, path[parent[e]][e])
            e = parent[e]
        e = end
        while e != start:
            path[parent[e]][e] -= flow
            e = parent[e]
        maxflow += flow
    return maxflow


def bfs(start, end, path, parent):
    visited = {}
    search = [start]
    while len(search) > 0:
        node = search.pop(0)
        for n in range(len(path)):
            if n not in visited and path[node][n] > 0:
                visited[n] = True
                parent[n] = node
                search.append(n)
    return end in visited


print(solution(
    [0], [3],
    [[0, 7, 0, 0],
     [0, 0, 6, 0],
     [0, 0, 0, 8],
     [9, 0, 0, 0]]))

print(solution(
    [0, 1], [4, 5],
    [[0, 0, 4, 6, 0, 0],
     [0, 0, 5, 2, 0, 0],
     [0, 0, 0, 0, 4, 4],
     [0, 0, 0, 0, 6, 6],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]))
