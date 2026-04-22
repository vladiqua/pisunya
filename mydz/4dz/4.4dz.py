color1 = input()
color2 = input()

colors = {'красный', 'синий', 'желтый'}

if color1 not in colors or color2 not in colors:
    print("ошибка цвета")
else:
    if color1 == color2:
        print(color1)
    else:
        pair = {color1, color2}

        if pair == {'красный', 'синий'}:
            print('фиолетовый')
        elif pair == {'красный', 'желтый'}:
            print('оранжевый')
        elif pair == {'синий', 'желтый'}:
            print('зеленый')
