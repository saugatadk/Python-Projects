class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag
    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary
        result = Complex(result_real, result_imaginary)
        return result
n1 = Complex(1, 9)
n2 = Complex(2, 10)
n3 = n1.add(n2)
print(f"Real:", n3.real)
print(f"Imaginary:", n3.imaginary)