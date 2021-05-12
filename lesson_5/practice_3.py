f = open("salaries.dat", "r", encoding="utf-8")
content = f.readlines()
f.close()
n = len(content)
sum = 0
for new_string in content:
    new_string = new_string.split()
    sum += int(new_string[1])
    if int(new_string[1]) < 20000:
        print(new_string[0])
print(f"Средняя з/п: {sum/n}")
