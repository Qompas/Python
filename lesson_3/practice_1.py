def div(m, n):
    try:
        return int(m) / int(n)
    except ZeroDivisionError:
        print('ОШИБКА! Делить на ноль нельзя')


inp = input("Введите числа через пробел: ").split()
print(div(inp[0], inp[1]))
