def is_divisible_by_3(n: int) -> bool:
    return n % 3 == 0


try:
    x = int(input("Введите число: "))
    if is_divisible_by_3(x):
        print("Делится на 3")
    else:
        print("Не делится на 3")
except ValueError:
    print("Ошибка: нужно ввести целое число")