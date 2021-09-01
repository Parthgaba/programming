all_sub = []


def subsequence(s, binary, length):
    sub = ""
    for j in range(length):
        if (binary & (1 << j)):
            sub += s[j]
    return sub


def possibleSubsequences(s):
    length = len(s)
    limit = 2 ** length
    for i in range(limit//2, limit-1):
        all_sub.append(subsequence(s, i, length))


if __name__ == "__main__":
    n = int(input())
    # exec
    lis = list(map(str,input().split()))
    st = ''.join(lis)
    temp = ''
    possibleSubsequences(st)
    #printSubsequence(lis,temp)
    print(all_sub)
    mn = 10**10
    fin_sum = 0
    total_sum = sum(map(int,list(st)))
    temp = 0
    for i in range(len(all_sub)):
        if len(all_sub[i])==n:
            continue
        if all_sub[i] == '':
            continue
        else:
            print('=>',all_sub[i])
            s = sum(list(map(int,list(all_sub[i]))))
            temp = total_sum-s
            print(s,temp,abs(temp-s))
        if mn > abs(temp-s):
            mn = abs(temp-s)
    print(mn)
