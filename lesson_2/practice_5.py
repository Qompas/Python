list_5 = [7, 5, 3, 3, 2]
new_el = int(input("Введите число:"))
i = 0
for n in list_5:
    if new_el <= n:
        i += 1
list_5.insert(i, new_el)
print(list_5)