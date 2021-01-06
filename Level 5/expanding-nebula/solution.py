import time

O = True
_ = False


def solution(g):
    cols = []
    for bitlist in zip(*g):
        n = 0
        for bit in bitlist:
            n = n << 1 | bit
        cols.append(n)
    return dfs(nodes_list(cols, len(g)), {})


def dfs(nodes_list, mem, depth=0, node=()):
    if depth == len(nodes_list):
        return 1
    key = (depth,) + node
    if key in mem:
        return mem[key]
    mem[key] = 0
    for adj in nodes_list[depth]:
        if not node or node[1] == adj[0]:
            mem[key] += dfs(nodes_list, mem, depth + 1, adj)
    return mem[key]


def nodes_list(cols, h):
    nodes_list = [[] for _ in cols]
    for n1 in range(2 << h):
        for n2 in range(2 << h):
            img = col_img((n1, n2), h)
            for idx, col in enumerate(cols):
                if col == img:
                    nodes_list[idx].append((n1, n2))
    return nodes_list


def col_img(pre, h):
    n = 0
    for idx in range(h):
        c = ((pre[0] >> idx & 1) +
             (pre[1] >> idx & 1) +
             (pre[0] >> (idx + 1) & 1) +
             (pre[1] >> (idx + 1) & 1))
        n = (n << 1) + (c == 1)
    return n


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
