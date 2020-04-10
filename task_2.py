def even(x):
    y = 0
    for i in x:
        if int(i) % 2 == 0:
            y += 1
    return str(y)


def uneven(x):
    y = 0
    for i in x:
        if int(i) % 2 != 0:
            y += 1
    return str(y)


a = input(f'Введите число : ')
print(f'{even(a)} четные')
print(f'{uneven(a)} нечетные')