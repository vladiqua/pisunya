def is_lucky(ticket: str) -> bool:
    ticket = ticket.strip()
    if (len(ticket) == 0) or (len(ticket) % 2 != 0) or (not ticket.isdigit()):
        return False
    half = len(ticket) // 2
    left = sum(int(ch) for ch in ticket[:half])
    right = sum(int(ch) for ch in ticket[half:])
    return left == right


t = input("Введите номер билета: ")
if is_lucky(t):
    print("Счастливый билет")
else:
    print("Не счастливый билет")