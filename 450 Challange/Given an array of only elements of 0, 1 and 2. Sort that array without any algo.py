n = int(input())
arr = list(map(int, input().split()))
zero, one = 0, 0
for i in arr:
    zero += 1 if i == 0 else 0
    one += 1 if i == 1 else 0
for j in range(n):
    if zero:
        arr[j] = 0
        zero -= 1
    elif one:
        arr[j] = 1
        one -= 1
    else:
        arr[j] = 2
print(*arr)
