while True:
    n = int(input())
    if n == -1:
        break
    else:
        s = 0
        arr = []
        for i in range(n):
            arr.append(int(input()))
        s = sum(arr)
        avg = s / n
        fin_sum = 0
        if avg - float(int(avg)) != 0:
            print(-1)
        else:
            for j in range(len(arr)):
                if arr[j] < avg:
                    fin_sum += abs(avg - arr[j])
            print(int(fin_sum))
