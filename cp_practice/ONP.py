import string

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)
for _ in range(int(input())):
    string = input()
    constants = []
    for i in string:
        if i == "(":
            constants.append("(")
        elif i == ")":
            while len(constants) > 0:
                if constants[len(constants) - 1] == "(":
                    constants.pop()
                    break
                else:
                    print(constants.pop(), end="")
        elif i in alphabets:
            print(i, end="")
        else:
            constants.append(i)
    print()
