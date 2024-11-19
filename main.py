class Calculator:
    def __init__(self):
        self.switcher = {
            '+': self.add,
            '-': self.sub,
            '*': self.mul,
            '/': self.div,
            '^': self.pow
        }

    def menu(self):
        print("Calculator - Choose an operation:")
        for key in self.switcher.keys():
            print(key)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero!"

    def pow(self, a, b):
        return a ** b

    def operation(self, op, a, b):
        func = self.switcher.get(op)
        if func:
            return func(a, b)
        else:
            return "Invalid operation!"

def main():
    calc = Calculator()
    calc.menu()
    op = input("Enter Choice (+, -, *, /, ^): ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = calc.operation(op, a, b)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
