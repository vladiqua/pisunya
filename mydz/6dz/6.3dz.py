def is_magic_date(date_str: str) -> bool:
    date_str = date_str.strip()
    parts = date_str.split(".")
    if len(parts) != 3:
        return False

    day_s, month_s, year_s = parts
    if not (day_s.isdigit() and month_s.isdigit() and year_s.isdigit()):
        return False

    day = int(day_s)
    month = int(month_s)
    year = int(year_s)

    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False

    return day * month == (year % 100)


s = input("Введите дату (дд.мм.гггг): ")
if is_magic_date(s):
    print("Магическая дата")
else:
    print("Не магическая дата")