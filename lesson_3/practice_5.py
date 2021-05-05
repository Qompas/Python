def practice_5():
    sum = 0
    while True:
        list_1 = input("Введите числа через пробел, введите ! через пробел чтобы завершить: \n").split()
        for a in list_1:
            if a == "!":
                print(f"Сумма = {sum}")
                return
            try:
                a = float(a)
            except ValueError:
                print('ОШИБКА! Вводите числа или !')
                break
            else:
                sum += a
        print(f"Сумма = {sum}")
    return


practice_5()
