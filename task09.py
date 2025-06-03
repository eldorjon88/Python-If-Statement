a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Teng tomonli")
    elif a == b or b == c or a == c:
        print("Teng yonli")
    else:
        print("Turli tomonli")
else:
    print("Uchburchak emas")
