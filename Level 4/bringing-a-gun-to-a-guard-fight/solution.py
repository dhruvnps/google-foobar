import math


def solution(dims, a, b, dist):
    a_mirr = mirr_vals(dist, dims, a)
    b_mirr = mirr_vals(dist, dims, b)
    vectors = []
    dists = {}
    for mirr in [a_mirr, b_mirr]:
        for x in mirr[0]:
            for y in mirr[1]:
                d = ((x - a[0]) ** 2 + (y - a[1]) ** 2)
                v = math.atan2(y - a[1], x - a[0])
                if d <= dist ** 2 and d != 0:
                    if not (v in dists and dists[v] <= d):
                        dists[v] = d
                        if mirr == b_mirr:
                            vectors.append(v)
    return len(set(vectors))


def mirr_vals(dist, dims, pt):
    w, h = [(pt[i], dims[i] - pt[i]) for i in [0, 1]]
    x, y = pt
    x_vals, y_vals = [x, -x], [y, -y]
    for i in range(-1, dist // min(dims)):
        x += w[i & 1] * 2
        y += h[i & 1] * 2
        x_vals.extend([x, -x])
        y_vals.extend([y, -y])
    return x_vals, y_vals


print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
print(solution([2, 5], [1, 2], [1, 4], 11))  # 27
print(solution([23, 10], [6, 4], [3, 2], 23))  # 8
print(solution([10, 10], [4, 4], [3, 3], 5000))  # 739323
