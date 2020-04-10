def sum_n(a, b, c, n):
    if b == n:
        return f' {c}'
    if b < n:
        return f'{sum_n(a/ -2, b + 1, c + a, n)}'


n = int(input("Введите количество элементов ряда чисел: "))
a = 1
b = 0
c = 0
print(sum_n(a, b, c, n))