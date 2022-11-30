from math import gcd


class Rational:
    def __init__(self, num=1, denom=2):
        if denom == 0:
            raise ZeroDivisionError
        if not isinstance(num, int):
            raise TypeError("Wrong argument(s)")
        if not isinstance(denom, int):
            raise TypeError("Wrong argument(s)")
        self._num = num
        self._denom = denom

    def ab_form(self):
        if self._num == self._denom:
            return 1
        else:
            return f"{self._num // gcd(self._num, self._denom)}/{self._denom // gcd(self._num, self._denom)}"

    def float_form(self):
        if self._num == self._denom:
            return 1
        else:
            return self._num / self._denom

    def __add__(self, other):
        num = self._num * other._denom + other._num * self._denom
        denom = self._denom * other._denom
        return Rational(num, denom).ab_form()

    def __sub__(self, other):
        num = self._num * other._denom - other._num * self._denom
        denom = self._denom * other._denom
        return Rational(num, denom).ab_form()

    def __mul__(self, other):
        num = self._num * other._num
        denom = self._denom * other._denom
        return Rational(num, denom).ab_form()

    def __truediv__(self, other):
        num = self._num * other._denom
        denom = self._denom * other._num
        return Rational(num, denom).ab_form()

    def __gt__(self, other):
        return self.float_form() > other.float_form()

    def __ge__(self, other):
        return self.float_form() >= other.float_form()

    def __lt__(self, other):
        return self.float_form() < other.float_form()

    def __le__(self, other):
        return self.float_form() <= other.float_form()


r1 = Rational(1, 2)
r2 = Rational(1, 4)
r3 = Rational(1, 8)

print(r1 + r2)
print(r2 / r1)
print(r3 > r2)

