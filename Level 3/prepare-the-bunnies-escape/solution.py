import time


def solution(map):
    w, h = len(map[0]), len(map)
    start = (0, 0)
    end = (w - 1, h - 1)
    # start, end = end, start
    connections = bfs(start, map, h, w)
    nxt = end
    dist = 0
    while nxt != start:
        if nxt not in connections:
            return -1
        nxt = connections[nxt]
        dist += 1
    return dist


def get_neighbours(point, h, w):
    get = []
    neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for n in neighbours:
        y, x = [point[i] + n[i] for i in [0, 1]]
        if h > y >= 0 and w > x >= 0:
            get.append((y, x))
    return get


def bfs(point, map, h, w):
    connections = {}
    visited = {}
    search = []
    search.append(point)
    while len(search) > 0:
        node = search.pop(0)
        neighbours = get_neighbours(node, h, w)
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
