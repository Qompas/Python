from sys import argv

try:
    print(float(argv[1]) * float(argv[2]) + float(argv[3]))
except ValueError:
    print("ОШИБКА! Неверные значения параметров")
