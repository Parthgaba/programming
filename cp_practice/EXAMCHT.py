import math


def divisors(n):
    i = 1
    count = 0
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
        i = i + 1
    return count


for _ in range(int(input())):
    a, b = map(int, input().split())
    p = abs(a - b)
    if p == 0:
        print(-1)
    else:
        print(divisors(p))
