i = 0
my_list = input("Введите числа: ").split()
while 2 * (i + 1) < len(my_list):
    m = my_list[2 * i]
    my_list[2 * i] = my_list[2 * i + 1]
    my_list[2 * i + 1] = m
    i += 1
print(my_list)
