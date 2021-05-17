# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def  __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print(f"Я пишу письмо домой с помощью {self.title}")

class Pencil(Stationery):

    def draw(self):
        print(f"Я рисую портрет остро заточеным {self.title}")

class Handle(Stationery):

    def draw(self):
        print(f"Я обвощу объявления в газете своим {self.title}")

pen = Pen("Parker")
pen.draw()
pencil = Pencil("KOH-I-NOOR")
pencil.draw()
handle = Handle("Brauberg")
handle.draw()
brush = Stationery("Mont Marte")
brush.draw()