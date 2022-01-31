a = complex(1, 2)
b = complex(3, 4)
c = complex(5, 6)

print(f'Даны компл. числа: a={a}, b={b}, c={c}')


class Complex:
    def __init__(self, num):
        self.r, self.i = num.real, num.imag

    def __str__(self):
        return str(complex(self.r, self.i))                             # для вывода строкой

    def __add__(self, other):
        return Complex(complex(self.r + other.r, self.i + other.i))     # отдельно суммы действ. и мним. частей

    def __mul__(self, other):
        return Complex(complex((self.r * other.r - self.i * other.i), (self.r * other.i + other.r * self.i)))

    @property
    def value(self):
        return complex(self.r, self.i)  # нормальная альтернатива перегрузке __str__


x = Complex(a)
y = Complex(b)
z = Complex(c)

# print(complex(x.r, x.i), complex(y.r, y.i), complex(z.r, z.i))

print(f'Сумма чисел a, b, c равна (встроенная математика): {a + b + c}')
# print(f'Сумма чисел a, b, c равна (через собственный класс "Complex"): {x + y + z}')
print(f'Сумма чисел a, b, c равна (через собственный класс "Complex"): {(x + y + z).value}')

print(f'Произведение чисел a, b, c равно (встроенная математика): {a * b * c}')
# print(f'Произведение чисел a, b, c равно (через собственный класс "Complex"): {x * y * z}')
print(f'Произведение чисел a, b, c равно (через собственный класс "Complex"): {(x * y * z).value}')
