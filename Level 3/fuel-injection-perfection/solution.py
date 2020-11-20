def solution(n):
    n = int(n)
    c = 0
    while n != 1 and n != 3:
        if not n & 1:
            n = n >> 1
        elif n >> 1 & 1:
            n += 1
        else:
            n -= 1
        c += 1
    return c + n - 1


print(solution('15'))
print(solution('4'))
