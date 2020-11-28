def f(dimensions, a, b, distance):
    d2 = distance ** 2
    w, h = [(b[i], dimensions[i] - b[i]) for i in [0, 1]]
    x, y = b
    x_vals, y_vals = [x, -x], [y, -y]
    for i in range(-1, distance // min(dimensions)):
        x += w[i & 1] * 2
        y += h[i & 1] * 2
        x_vals.extend([x, -x])
        y_vals.extend([y, -y])
    vectors = []
    for x in x_vals:
        for y in y_vals:
            d = ((x - a[0]) ** 2 + (y - a[1]) ** 2)
            if d < d2:
                vector = (x - a[0], y - a[1])
                if not any(equals(v, vector) for v in vectors):
                    vectors.append(vector)
    return vectors


def equals(m, n):
    if m[0] == n[0] == 0 or m[1] == n[1] == 0:
        return True
    if n[0] == 0 or n[1] == 0:
        return False
    if not (m[1] ^ n[1] >= 0 and m[0] ^ n[0] >= 0):
        return False
    return m[0] / float(n[0]) == m[1] / float(n[1])


def solution(dimensions, a, b, distance):
    l1 = f(dimensions, a, b, distance)
    l2 = f(dimensions, a, a, distance)

    c = 0
    for i in l2:
        for j in l1:
            if equals(i, j) and i != (0, 0) and j != (0, 0) and abs(i[0]) <= abs(j[0]):
                c += 1

    return len(l1) - c


print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
print(solution([2, 5], [1, 2], [1, 4], 11))  # 27
print(solution([23, 10], [6, 4], [3, 2], 23))  # 8
print(solution([10, 10], [4, 4], [3, 3], 5000))  # 739323

'''
def solution(dimensions, a, b, distance):
    w, h = [(b[i], dimensions[i] - b[i]) for i in [0, 1]]
    x, y = b
    x_vals, y_vals = [x, -x], [y, -y]
    for i in range(-1, distance // min(dimensions)):
        x += w[i & 1] * 2
        y += h[i & 1] * 2
        x_vals.extend([x, -x])
        y_vals.extend([y, -y])
    vectors = []
    for x in x_vals:
        for y in y_vals:
            d = ((x - a[0]) ** 2 + (y - a[1]) ** 2) ** 0.5
            if d < distance:
                vector = (x - a[0], y - a[1])
                if not any(equals(v, vector) for v in vectors):
                    vectors.append(vector)
    return len(vectors)


def equals(m, n):
    if m[0] == n[0] == 0 or m[1] == n[1] == 0:
        return True
    if n[0] == 0 or n[1] == 0:
        return False
    if not (m[1] ^ n[1] >= 0 and m[0] ^ n[0] >= 0):
        return False
    return m[0] / float(n[0]) == m[1] / float(n[1])
'''
