class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    def evaluate(self, x):
        result = 0
        for power, coefficient in self.coefficients.items():
            result += coefficient * (x ** power)
        return result
f = Polynomial({4: 6, 2: 2, 0: 3})
x_value = 91
result = f.evaluate(x_value)
print(f"f({x_value}) = {result}")
