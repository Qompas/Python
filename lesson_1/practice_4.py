n = int(input("Введите целое положительное число: "))
m = 0
while n != 0:
    d = n % 10
    n = n // 10
    if d > m:
        m = d
print(m)
