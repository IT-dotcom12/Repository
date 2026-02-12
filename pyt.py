binary = input("Введите двоичное число:")

t=True

if binary == "":
    t=False
else:
    for c in binary:
        if c != "0" and c!="1":
            t=False
            break
if t:
    if binary[-1] == "0":
        print("Чётное")
    else:
        print("Нечётное")
else:
    print("Это не двоичное число")
