def gcd(n1, n2) :
    if n1 == 0 and n2 == 0 :
        raise ArithmeticError("gcd(0,0) does not exist")
    if n1 == 0 :
        return n2
    if n2 == 0 :
        return n1

    while True:
        r = n1 % n2
        if not r:
            break
        n1 = n2
        n2 = r
    return n2

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

        self.normalize()
    
    def normalize(self):
        if self.denom == 0 :
            raise ArithmeticError("denom cannot be zero")

        if self.denom < 0 :
            self.numer = self.numer * (-1)
            self.denom = self.denom * (-1)

        tmp_gcd = gcd(self.numer, self.denom)
        self.numer = self.numer // tmp_gcd
        self.denom = self.denom // tmp_gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
