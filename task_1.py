# https://drive.google.com/file/d/1aJh0Dx7sSOOsOkXB4my1lgO9KCZ5jMUe/view?usp=sharing
a = int(input('Введите трехзначное число'))

b = (int(a / 100) + int((a / 10) % 10) + int(a % 10))

c = (int(a / 100) * int((a / 10) % 10) * int(a % 10))

print(f'Сумма цифр трехзначного числа {a} равна {b}')
print(f'Произведение цифр трехзначного числа {a} равно {c}')
