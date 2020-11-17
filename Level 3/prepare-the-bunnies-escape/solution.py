import time


def solution(map):
    h, w = len(map), len(map[0])
    distmap = [[1 for x in range(w)] for y in range(h)]
    visitmap = [[0 for x in range(w)] for y in range(h)]
    bfs((0, 0), map, h, w, distmap, visitmap)
    bfs((h - 1, w - 1), map, h, w, distmap, visitmap)
    vals = []
    for y in range(h):
        for x in range(w):
            if visitmap[y][x] == 2:
                vals.append(distmap[y][x])
    return(min(vals))


def get_neighbours(point, h, w):
    get = []
    neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for n in neighbours:
        y, x = [point[i] + n[i] for i in [0, 1]]
        if h > y >= 0 and w > x >= 0:
            get.append((y, x))
    return get


def bfs(start, map, h, w, distmap, visitmap):
    visited = {}
    search = []
    search.append((start, 0, False))
    while len(search) > 0:
        (point, dist, is_wall) = search.pop(0)
        if point != start:
            distmap[point[0]][point[1]] += dist
            visitmap[point[0]][point[1]] += 1
        if not is_wall:
            neighbours = get_neighbours(point, h, w)
            for n in neighbours:
                if n not in visited:
                    n_is_wall = map[n[0]][n[1]] == 1
                    search.append((n, dist + 1, n_is_wall))
                    visited[n] = point


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
