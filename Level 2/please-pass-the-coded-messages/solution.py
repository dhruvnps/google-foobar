def solution(l):
    l.sort()
    r = remainder(l)
    if r != 0:
        mod = [[], [], []]
        for i in l:
            mod[i % 3].append(i)
        if len(mod[r]) > 0:
            l.remove(mod[r][0])
        elif len(mod[(1 - r) + 2]) > 1:
            l.remove(mod[(1 - r) + 2][0])
            l.remove(mod[(1 - r) + 2][1])
        else:
            return 0
    return reverse_joined(l)


def remainder(l):
    return sum(l) % 3


def reverse_joined(l):
    return sum(i * 10**x for x, i in enumerate(l))


print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
print(solution([1, 1, 1, 1, 1]))
