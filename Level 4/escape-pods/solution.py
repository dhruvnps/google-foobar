def solution(entrances, exits, path):
    maxflow = 0
    parent = {}
    start, end = terminal_nodes(entrances, exits, path)
    while bfs(start, end, path, parent):
        flow = float('inf')
        n = end
        while n != start:
            flow = min(flow, path[parent[n]][n])
            n = parent[n]
        n = end
        while n != start:
            path[parent[n]][n] -= flow
            path[n][parent[n]] += flow
            n = parent[n]
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


def terminal_nodes(entrances, exits, path):
    path.extend([[0] * len(path) for _ in range(2)])
    for n in entrances:
        path[-2][n] = float('inf')
    for n in range(len(path)):
        path[n].extend([0, float('inf') if n in exits else 0])
    return len(path) - 2, len(path) - 1


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
