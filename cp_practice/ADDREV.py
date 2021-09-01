for _ in range(int(input())):
    n, m = map(str, input().split())
    n = int(n[::-1])
    m = int(m[::-1])
    res = int(str(n + m)[::-1])
    print(res)
