import time

O = True
_ = False


def solution(g):
    return dfs(nodes_list(cols(g), len(g)), 0, None, {})


def dfs(nodes_list, depth, node, mem):
    if node != None and tuple([depth] + node) in mem:
        return mem[tuple([depth] + node)]
    c = 0
    if depth == len(nodes_list):
        return 1
    for nxt_node in nodes_list[depth]:
        if node == None or nxt_node[0] == node[1]:
            c += dfs(nodes_list, depth + 1, nxt_node, mem)
    if node != None:
        mem[tuple([depth] + node)] = c
    return c


def nodes_list(cols, h):
    nodes_list = [[] for _ in cols]
    for n1 in range(2 ** (h + 1)):
        for n2 in range(2 ** (h + 1)):
            nxt_col = nxt([n1, n2], h)
            for idx, col in enumerate(cols):
                if col == nxt_col:
                    nodes_list[idx].append([n1, n2])
    return nodes_list


def nxt(prev, h):
    n = 0
    for idx in range(h):
        c = ((prev[0] >> idx & 1) +
             (prev[1] >> idx & 1) +
             (prev[0] >> (idx + 1) & 1) +
             (prev[1] >> (idx + 1) & 1))
        n = (n << 1) + (c == 1)
    return n


def cols(g):
    cols = []
    for idx in range(len(g[0])):
        n = 0
        for i in g:
            n = (n << 1) + i[idx]
        cols.append(n)
    return cols


# 4
t1 = time.perf_counter()
print(solution(
    [[O, _, O],
     [_, O, _],
     [O, _, O]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

# 11567
t1 = time.perf_counter()
print(solution(
    [[O, O, _, O, _, O, _, O, O, _],
     [O, O, _, _, _, _, O, O, O, _],
     [O, O, _, _, _, _, _, _, _, O],
     [_, O, _, _, _, _, O, O, _, _]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

# 254
t1 = time.perf_counter()
print(solution(
    [[O, _, O, _, _, O, O, O],
     [O, _, O, _, _, _, O, _],
     [O, O, O, _, _, _, O, _],
     [O, _, O, _, _, _, O, _],
     [O, _, O, _, _, O, O, O]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))
