# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class FatalError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.contained_items = {}

    def __str__(self):
        return self.name

    def add_items(self, obj, n=1):
        if self.contained_items.get(obj.name) == None:
            self.contained_items[obj.name] = n
        else:
            self.contained_items[obj.name] += n

    def substract_items(self, obj, n=1):
        if self.contained_items.get(obj.name) == None or self.contained_items.get(obj.name) < n:
            print(f"Can't get {obj.name} from {self.name}")
        else:
            self.contained_items[obj.name] += -n
        if self.contained_items[obj.name] == 0:
            self.contained_items.pop(obj.name)

    @classmethod
    def create_warehouse(cls):
        name = input("Введите имя склада: ")
        return Warehouse(name)


class OfficeEquipment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, name, chromatic_printing):
        super().__init__(name)
        self.chromatic_printing = chromatic_printing

    @classmethod
    def create_item(cls):
        name = input("Введите название принтера: ")
        chromatic_printing = int(input("Введите '1', если возможна цветная печать, иначе введите '0': "))
        try:
            if chromatic_printing == 0:
                chromatic_printing = False
            elif chromatic_printing == 1:
                chromatic_printing = True
            else:
                raise FatalError("ОШИБКА!")
        except FatalError as err_msg:
            print(err_msg)
            exit(1)
        return Printer(name, chromatic_printing)


class Scanner(OfficeEquipment):
    def __init__(self, name, chromatic_scanning):
        super().__init__(name)
        self.chromatic_scanning = chromatic_scanning

    @classmethod
    def create_item(cls):
        name = input("Введите название сканера: ")
        chromatic_scanning = int(input("Введите '1', если возможно цветное сканирование, иначе введите '0': "))
        try:
            if chromatic_scanning == 0:
                chromatic_scanning = False
            elif chromatic_scanning == 1:
                chromatic_scanning = True
            else:
                raise FatalError("ОШИБКА!")
        except FatalError as err_msg:
            print(err_msg)
            exit(1)
        return Scanner(name, chromatic_scanning)


class Xerox(OfficeEquipment):
    def __init__(self, name, chromatic_printing, chromatic_scanning):
        super().__init__(name)
        self.chromatic_printing = chromatic_printing
        self.chromatic_scanning = chromatic_scanning

    @classmethod
    def create_item(cls):
        name = input("Введите название ксерокса: ")
        chromatic_printing = int(input("Введите '1', если возможна цветная печать, иначе введите '0': "))
        try:
            if chromatic_printing == 0:
                chromatic_printing = False
            elif chromatic_printing == 1:
                chromatic_printing = True
            else:
                FatalError("ОШИБКА!")
        except FatalError as err_msg:
            print(err_msg)
            exit(1)
        chromatic_scanning = int(input("Введите '1', если возможно цветное сканирование, иначе введите '0': "))
        try:
            if chromatic_scanning == 0:
                chromatic_scanning = False
            elif chromatic_scanning == 1:
                chromatic_scanning = True
            else:
                raise FatalError("ОШИБКА!")
        except FatalError as err_msg:
            print(err_msg)
            exit(1)
        return Xerox(name, chromatic_printing, chromatic_scanning)


xerox_1 = Xerox.create_item()

warehouse_1 = Warehouse.create_warehouse()

warehouse_1.add_items(xerox_1, 3)

print(f"В складе {warehouse_1} находятся усройства {xerox_1} в количестве {warehouse_1.contained_items[xerox_1.name]}")
