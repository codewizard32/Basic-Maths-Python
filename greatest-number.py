def greatest_number(a, b, c):
    if a > b and a > c:
        print("Greatest number is :", a)
    elif b > a and b > c:
        print("Greatest number is :", b)
    else:
        print("Greatest number is :", c)

a, b, c = map(int, input().split())
greatest_number(a, b, c)
