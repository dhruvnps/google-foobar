def solution(l):
    c = 0
    prev_y = [0 for i in range(len(l))]
    for i, x in enumerate(l):
        for j, y in list(enumerate(l))[i+1:]:
            if y % x == 0:
                prev_y[j] += 1
                c += prev_y[i]
    return c


print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))
print(solution([1] * 2000))


# def solution(l):
#     c = 0
#     for x, i in enumerate(l[:-2]):
#         c += triples(l, idx=x, pos=1)
#     return c
#
#
# def triples(l, idx, pos):
#     if pos == 3:
#         return 1
#     c = 0
#     nxt_idx = idx+1
#     nxt_l = l[nxt_idx:]
#     if len(nxt_l) > 0:
#         for x, i in enumerate(nxt_l):
#             if i >= l[idx] and i % l[idx] == 0:
#                 c += triples(l, x + nxt_idx, pos + 1)
#     return c
