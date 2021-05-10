my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(my_list[1:]) if my_list[i + 1] > my_list[i]]
print(new_list)
