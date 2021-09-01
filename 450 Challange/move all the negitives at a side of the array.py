n = int(input())
lis = list(map(int, input().split()))
j = 0
for _ in range(len(lis)):
    if lis[_] < 0:
        temp = lis[_]
        lis[_] = lis[j]
        lis[j] = temp
        j += 1
print(*lis)
