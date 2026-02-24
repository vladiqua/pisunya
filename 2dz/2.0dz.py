r = float(input("Введите радиус: "))
pi = 3.14159
S = pi * r ** 2

print("Площадь круга:", S)
a = float(input("Введите a: "))
b = float(input("Введите b: "))

if a != 0:
    x = -b / a
    print("x =", x)
else:
    print("Уравнение не имеет решения")
