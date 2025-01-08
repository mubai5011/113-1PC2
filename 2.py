class Term:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
    def evaluate(self, x):
        return self.coefficient * (x ** self.exponent)
class Polynomial:
    def __init__(self):
        self.terms = []
    def add_term(self, coefficient, exponent):
        self.terms.append(Term(coefficient, exponent))
    def evaluate(self, x):
        result = 0
        for term in self.terms:
            result += term.evaluate(x)
        return result
polynomial = Polynomial()
polynomial.add_term(6, 4)  
polynomial.add_term(0, 3)  
polynomial.add_term(2, 2)  
polynomial.add_term(0, 1)  
polynomial.add_term(3, 0)  
x_value = 91
result = polynomial.evaluate(x_value)
print(f"f({x_value}) = {result}")
