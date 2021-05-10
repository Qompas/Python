my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_gen = [n for n in my_list if my_list.count(n) == 1]
print(my_gen)
