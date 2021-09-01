import math


def sieve(given):
    prime = [True] * given
    i = 2
    while i * i <= given:
        if prime[i]:
            for j in range(i * i, given, i):
                prime[j] = False
        i += 1
    primes = [x for x in range(2, len(prime)) if prime[x]]
    return primes


prime = sieve(10)


def segmentSieve(high, low):
    limit = int(math.floor(math.sqrt(high)) + 1)
    limit = sieve(limit)
    mark = [True for i in range(high - low + 1)]
    for i in range(len(limit)):
        loLim = int(math.floor(low / limit[i]) * limit[i])
        if loLim < low:
            loLim += limit[i]
        for j in range(loLim, high + 1, limit[i]):
            mark[j - low] = False
        if loLim == limit[i]:
            mark[loLim - low] = True
    mark = [low + x for x in range(len(mark)) if mark[x]]
    return mark


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    mark = segmentSieve(b, a)
    for i in mark:
        if i != 1:
            print(i)
