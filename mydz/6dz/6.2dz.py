def divide_100_by(x: float) -> float:
    return 100 / x


try:
    s = input("Введите число: ").replace(",", ".").strip()
    x = float(s)
    print(divide_100_by(x))
except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
except Exception:
    print("Ошибка: что-то пошло не так")