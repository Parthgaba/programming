n = int(input())
arr = list(map(int,input().split()))
i = 0
j = n-1
while i<=j:
    t = arr[j]
    arr[j] = arr[i]
    arr[i] = t
    i, j = i+1, j-1
print(arr)
