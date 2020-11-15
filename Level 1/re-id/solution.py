import time


def solution(i):
    primes = '23'
    n = 3
    while(len(primes) < i + 5):
        n += 2
        if odd_is_prime(n):
            primes += str(n)
    return primes[i:i+5]


def odd_is_prime(n):
    if n % 3 == 0:
        return False
    for i in range(6, int(n**0.5) + 2, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


t1 = time.perf_counter()
print(solution(10000))
t2 = time.perf_counter()
print('{:0.3} seconds'.format(t2 - t1))
