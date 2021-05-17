# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
# реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLights:
    __color = "Red"

    def running(self):
        while True:
            if self.__color == "Green":
                self.__color = "Red"
                print("Red")
                sleep(7)
                continue
            elif self.__color == "Red":
                self.__color = "Yellow"
                print("Yellow")
                sleep(2)
                continue
            elif self.__color == "Yellow":
                self.__color = "Green"
                print("Green")
                sleep(7)
                continue


traffic_light = TrafficLights()
traffic_light.running()
