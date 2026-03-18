n = int(input("Сколько слов вы хотите ввести? "))

result = ""
for i in range(n):
    word = input()
    if i == 0:
        result = word
    else:
        result += " " + word

print(result)