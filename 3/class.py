class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2


cal1 = Calculator(2,5)

print(cal1.add())
print(cal1.sub())








