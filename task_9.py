a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')

if a > b > c or a < b < c:
    print(f'Среднее число {b}')
elif b > a > c or b < a < c:
    print(f'Среднее число {a}')
else:
    print(f'Среднее число {c}')
