def isEven(num):
    return num % 2 == 0


questions = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    questions.append([a, b])

for item in questions:
    a, b = item[0], item[1]
    an = isEven(a)
    bn = isEven(b)
    if a - 2 == b or a == b:
        pass
    else:
        print("No Number")
        continue
    if an and bn:
        print(a + b)
    elif not an and not bn:
        print(a + b - 1)
    else:
        print("No Number")
