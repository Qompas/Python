# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        return Complex(
            (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
            (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2))

    def __str__(self):
        if self.imaginary < 0:
            output = f"{str(self.real)}-{str(abs(self.imaginary))}j"
        else:
            output = f"{str(self.real)}+{str(self.imaginary)}j"
        return output


a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a * b)
print(a / b)
