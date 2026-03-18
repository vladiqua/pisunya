result = ""
first = True

while True:
    word = input()
    if word == "stop":
        break
    if first:
        result = word
        first = False
    else:
        result += " " + word

print(result)