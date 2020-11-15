import time


def solution(map):
    w, h = len(map[0]), len(map)
    end = (h - 1, w - 1)
    connections = bfs((0, 0), map, end)
    nxt = end
    dist = 0
    while nxt != (0, 0):
        if nxt not in connections:
            return -1
        nxt = connections[nxt]
        dist += 1
    return dist


def get_neighbours(point, end):
    get = []
    neighbours = [(-1, +0), (+0, -1), (+0, +1), (+1, +0)]
    for n in neighbours:
        y, x = [point[i] + n[i] for i in [0, 1]]
        if end[0] >= y >= 0 and end[1] >= x >= 0:
            get.append((y, x))
    return get


def bfs(point, map, end):
    connections = {}
    visited = {}
    search = []
    search.append(point)
    while len(search) > 0:
        node = search.pop(0)
        neighbours = get_neighbours(node, end)
        for n in neighbours:
            if n not in connections and map[n[0]][n[1]] != 1:
                search.append(n)
                connections[n] = node
    return connections


t1 = time.perf_counter()
print(solution(
    [[0, 1, 1, 0],
     [0, 0, 0, 1],
     [1, 1, 0, 0],
     [1, 1, 1, 0]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

t1 = time.perf_counter()
print(solution(
    [[0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

t1 = time.perf_counter()
print(solution(
    [[0, 1, 1],
     [0, 1, 1],
     [0, 1, 0]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

t1 = time.perf_counter()
print(solution(
    [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))
