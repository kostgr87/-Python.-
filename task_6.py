import random

attempt = 0
number = random.randint(0, 100)

while attempt < 10:
    answer = int(input(f'Нужно угадать число от 0 до 100, у вас 10 попыток : '))
    if answer == number:
        print(f'Вы угадали! Это число {number}')
        break
    elif answer > number:
        attempt += 1
        print(f'Вы ввели слишком большое число, попробуйте еще раз, осталось попыток = {10 - attempt}')
    else:
        attempt += 1
        print(f'Вы ввели слишком маленькое число, попробуйте еще раз, осталось попыток = {10 - attempt}')
