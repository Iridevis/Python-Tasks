a, b, c = map(int, input().split())

if a == 0:
    if b != 0:
        x = -c / b
        print(round(x))
    elif c == 0:
        pass
    else:
        pass
else:
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        sqrt_discr = discr ** 0.5
        x1 = (-b + sqrt_discr) / (2 * a)
        x2 = (-b - sqrt_discr) / (2 * a)
        if x1 < x2:
            print(round(x1), round(x2))
        else:
            print(round(x2), round(x1))
    elif discr == 0:
        x = -b / (2 * a)
        print(round(x))
    else:
        pass
