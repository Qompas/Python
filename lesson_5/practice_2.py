f = open("newfile.dat", "r", encoding="utf-8")

content = f.readlines()
f.close()
print(f"Количество строк: {len(content)}")
for i, new_string in enumerate(content):
       print(f"Количество слов в строке {i + 1}: {len(new_string.split())}")
