def solution(entrances, exits, path):
    parent = {}
    maxflow = 0
    start = entrances[0]
    end = exits[0]
    while bfs(start, end, path, parent):
        flow = float('inf')
        e = end
        while e != start:
            flow = min(flow, path[parent[e]][e])
            e = parent[e]
        maxflow += flow
        e = end
        while e != start:
            path[parent[e]][e] -= flow
            e = parent[e]
    return maxflow


def bfs(start, end, path, parent):
    visited = {}
    search = [start]
    while len(search) > 0:
        node = search.pop(0)
        for n in range(len(path)):
            if n not in visited:
                if valid_traversal(node, n, path):
                    visited[n] = True
                    parent[n] = node
                    search.append(n)
    return end in visited


def valid_traversal(a, b, path):
    return path[a][b] > 0


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


# def solution(entrances, exits, path):
#     parent = {}
#     maxflow = 0
#     graph = {
#         'cap': path,
#         'flow': [[0] * len(path) for y in path]
#     }
#     while bfs(entrances[0], exits[0], graph, parent):
#         flow = float('inf')
#         e = exits[0]
#         s = entrances[0]
#         while e != s:
#             flow = min(flow, graph['cap'][parent[e]][e])
#             e = parent[e]
#         maxflow += flow
#         e = exits[0]
#         while e != s:
#             graph['cap'][parent[e]][e] -= flow
#             e = parent[e]
#     return maxflow


# def bfs(start, end, graph, parent):
#     visited = {}
#     search = [start]
#     while len(search) > 0:
#         node = search.pop(0)
#         for n in range(len(graph['cap'])):
#             if n not in visited:
#                 if valid_traversal(node, n, graph):
#                     visited[n] = True
#                     parent[n] = node
#                     search.append(n)
#     return end in visited


# def valid_traversal(a, b, graph):
#     return graph['cap'][a][b] > 0
