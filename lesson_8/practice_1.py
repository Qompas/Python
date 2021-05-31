# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_date(cls, obj):
        date = obj.date
        date = date.split('-')
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validate_date(obj):
        d, m, y = Date.extract_date(obj)
        if y <= 0 or d <= 0 or m <= 0:
            return False
        if y % 4 != 0:
            months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        else:
            months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if m > 12:
            return False
        elif d > months[m]:
            return False
        else:
            return True

date = Date("29-02-1996")
print(Date.extract_date(date))
print(Date.validate_date(date))
