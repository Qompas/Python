gain = int(input("Введите значение выручки: "))
loss = int(input("Введите значение издержек: "))
if gain > loss:
    print("Фирма работает в прибыль")
    print(f"Рентабельность выручки: {(gain - loss) / gain}")
    n = int(input("Введите число сотрудников:"))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {(gain - loss) / n}")
elif gain < loss:
    print("Фирма работает в убыток")
elif gain == loss:
    print("Фирма не прибыльна и не убыточна")
