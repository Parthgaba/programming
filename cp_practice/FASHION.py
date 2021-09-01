for _ in range(int(input())):
    len_hotness = int(input())
    men_hotness = list(map(int, input().split()))
    women_hotness = list(map(int, input().split()))
    men_hotness.sort()
    women_hotness.sort()
    product = 0
    for i in range(len_hotness):
        product += men_hotness[i] * women_hotness[i]
    print(product)
