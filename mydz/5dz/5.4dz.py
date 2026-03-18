import random

mistakes = 0
correct = 0

while mistakes < 3:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    
    answer = input(f"{a} + {b} = ")
    
    if not answer.lstrip("-").isdigit():
        print("Ответ неверный")
        mistakes += 1
        continue

    answer = int(answer)

    if answer == a + b:
        print(" Правильно!")
        correct += 1
    else:
        print(" Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct}")