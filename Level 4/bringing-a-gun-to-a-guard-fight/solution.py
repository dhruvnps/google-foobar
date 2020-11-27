def solution(dimensions, a, b, distance):
    w, h = [(b[i], dimensions[i] - b[i]) for i in [0, 1]]
    x, y = b
    x_vals, y_vals = [x, -x], [y, -y]
    t = 1
    for i in range(distance // min(dimensions) + 1):
        x += w[t] * 2
        y += h[t] * 2
        x_vals.extend([x, -x])
        y_vals.extend([y, -y])
        t = abs(t - 1)
    bearings = []
    for x in x_vals:
        for y in y_vals:
            d = ((x - a[0]) ** 2 + (y - a[1]) ** 2) ** 0.5
            if d < distance:
                bearings.append((x - a[0], y - a[1]))
    return len(bearings)


print(solution([3, 2], [1, 1], [2, 1], 4))
print(solution([300, 275], [150, 150], [185, 100], 500))
