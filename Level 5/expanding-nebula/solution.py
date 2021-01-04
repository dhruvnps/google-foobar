import time

O = True
_ = False


def solution(g):
    h = len(g)
    nodes_list = [preimages(col, h) for col in cols(g)]
    c = [0]
    dfs(None, nodes_list, 0, c)
    return c[0]


def dfs(node, nodes_list, depth, c):
    if depth == len(nodes_list):
        c[0] += 1
        return
    for nxt_node in nodes_list[depth]:
        if node == None or nxt_node[0] == node[1]:
            dfs(nxt_node, nodes_list, depth + 1, c)


def preimages(col, h):
    pre_list = []
    for n1 in range(2 ** (h + 1)):
        for n2 in range(2 ** (h + 1)):
            pre = [n1, n2]
            if check(pre, col, h):
                pre_list.append(pre)
    return pre_list


def cols(g):
    cols = []
    for idx in range(len(g[0])):
        n = 0
        for i in g:
            n = (n << 1) + i[idx]
        cols.append(n)
    return cols


def check(pre, col, h):
    for idx in range(h):
        c = ((pre[0] >> idx & 1) +
             (pre[1] >> idx & 1) +
             (pre[0] >> (idx + 1) & 1) +
             (pre[1] >> (idx + 1) & 1))
        if col >> idx & 1 != (c == 1):
            return False
    return True


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
