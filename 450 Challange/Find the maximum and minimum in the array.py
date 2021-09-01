n = int(input())
arr = list(map(int,input().split()))
mx = 0
mn = arr[0]
for i in range(n):
    if mx < arr[i]:
        mx = arr[i]
    if mn > arr[i]:
        mn = arr[i]
print(mx, mn)
