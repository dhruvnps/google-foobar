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
