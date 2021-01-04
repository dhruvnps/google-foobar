import time

O = True
_ = False


def solution(g):
    nodes_list = [preimages(col) for col in cols(g)]
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


def preimages(col):
    pre_list = []
    l = len(col) + 1
    for n in range(2 ** (l * 2)):
        b = format(n, 'b').zfill(l * 2)
        pre = [b[:l], b[l:]]
        if check(pre, col):
            pre_list.append(pre)
    return pre_list


def cols(g):
    cols = []
    for idx in range(len(g[0])):
        cols.append('')
        for i in g:
            cols[idx] += '1' if i[idx] else '0'
    return cols


def check(pre, col):
    for idx, i in enumerate(col):
        c = sum([int(pre[0][idx]),
                 int(pre[1][idx]),
                 int(pre[0][idx + 1]),
                 int(pre[1][idx + 1])])
        if int(i) != (c == 1):
            return False
    return True


# 11567
t1 = time.perf_counter()
print(solution(
    [[O, O, _, O, _, O, _, O, O, _],
     [O, O, _, _, _, _, O, O, O, _],
     [O, O, _, _, _, _, _, _, _, O],
     [_, O, _, _, _, _, O, O, _, _]]))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))

# 4
t1 = time.perf_counter()
print(solution(
    [[O, _, O],
     [_, O, _],
     [O, _, O]]))
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
