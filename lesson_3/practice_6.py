def int_func(word):
    return word.title() if word.isascii() and word.isalpha() and word.islower() else None


list_1 = input('Введите строку, используя только строчные латинские буквы: \n').split()
for i, a in enumerate(list_1):
    list_1[i] = int_func(a)
try:
    string_1 = " ".join(list_1)
    print(string_1)
except TypeError:
    print("ОШИБКА!")
