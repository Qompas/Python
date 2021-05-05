def my_func(a, b):
    try:
        x = float(a)
        y = int(b)
    except ValueError:
        print('ОШИБКА! Введите действительное a и целое b')
        return
    if a <= 0 or b >= 0:
        print('ОШИБКА! Введите положительное a и отрицательное b')
        return
    return a ** b


print(my_func(4, -5))
