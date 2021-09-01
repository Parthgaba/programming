lis1 = list(map(int, input().split()))
lis2 = list(map(int, input().split()))
fin_lis = lis1+lis2
fin_lis.sort()
c = 0
for i in range(len(fin_lis)):
    if fin_lis[i]==fin_lis[i-1]:
        c += 1

print(len(fin_lis)-c)