# https://drive.google.com/file/d/1x4cmgbLD0nIm53rX0zrR11pM8W7P2qOp/view?usp=sharing

b = 1
while b != 0:
    def my_func(a, b, c):
        if c == '/':
            return f' Деление чисел равно {a / b}'
        elif c == '*':
            return f' Произведение чисел равно {a * b}'
        elif c == '+':
            return f' Сумма чисел равна {a + b}'
        elif c == '-':
            return f' Вычитание чисел равно {a - b}'


    a = int(input(f'Введите первое число : '))
    b = int(input(f'Введите второе число : '))
    c = input(f'Введите знак операции +, -, *, / или 0 для выхода : ')
    if c == '0':
        print(f'Программа завершена')
        break
    elif c == '/':
        if b == 0:
            print(f' На ноль делить нельзя')
        else:
            print(my_func(a, b, c))
    elif c == '*' or c == '+' or c == '-':
        print(my_func(a, b, c))
    else:
        print(f'Вы ввели неверный знак, введите: +, -, *, / или 0 для выхода :')