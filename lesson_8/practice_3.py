# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


list_1 = []

while True:
    string_1 = input("Введите число, введите 'stop' чтобы завершить: ")
    if string_1 == "stop":
        break
    try:  # проверяем посимвольно введенные данные, если введено действительное число, оно заносится в список
        split_string = string_1.split(".")
        if len(split_string) > 2:
            raise MyErr("ERROR!")
        if ord(string_1[0][0]) != 45 and (ord(split_string[0][0]) < 48 or ord(split_string[0][0]) > 57):
            raise MyErr("ERROR!")
        for el in split_string[0][1:]:
            if 48 > ord(el) or ord(el) > 57:
                raise MyErr("ERROR!")
        if len(split_string) == 2:
            for el in split_string[1]:
                if 48 > ord(el) or ord(el) > 57:
                    raise MyErr("ERROR!")
    except MyErr as err:
        print(err)
        continue
    list_1.append(float(string_1))
