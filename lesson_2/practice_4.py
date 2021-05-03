string_4 = input("Введите строку: ").split()
for i, el in enumerate(string_4):
    print(f'{i + 1}: {el[:10]}')
