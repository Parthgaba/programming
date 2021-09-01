while True:
    a, b, c = map(int, input().split())
    if a == b and c == b and a == 0:
        break
    else:
        if c - b == b - a:
            print("AP", c + (c - b))
        else:
            if c == 0:
                print("GP", 0)
            else:
                if c / b != c // b:
                    print("GP", c * (c / b))
                else:
                    print("GP", c * (c // b))
