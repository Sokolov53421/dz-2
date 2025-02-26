from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)

    def __mul__(self, other):
        """Множення дробів."""
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(num, den)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'Fraction: {self.numerator}, {self.denominator}'


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
