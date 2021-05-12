f = open("newfile.dat", "w", encoding="utf-8")
print("Вводите данные построчно, введите пустую строку чтобы закончить ввод")

while True:
    s = input()
    if s == "":
        break
    f.write(s + "\n")

f.close()
