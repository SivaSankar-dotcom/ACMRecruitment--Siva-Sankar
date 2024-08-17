import re
import math

class CalculatorError(Exception):
    pass

class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize(expression)
    
    def tokenize(self, expression):
        # Tokenize the input expression into numbers, operators, and parentheses
        token_pattern = re.compile(r'\s*(\d+|\S)\s*')
        tokens = token_pattern.findall(expression)
        return tokens
    
    def parse(self):
        # Convert tokens to a list of values and operators
        output = []
        operators = []
        
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        def apply_operator(op):
            b = output.pop()
            a = output.pop()
            if op == '+':
                output.append(a + b)
            elif op == '-':
                output.append(a - b)
            elif op == '*':
                output.append(a * b)
            elif op == '/':
                if b == 0:
                    raise CalculatorError("Division by zero")
                output.append(a / b)
            elif op == '^':
                output.append(a ** b)
        
        for token in self.tokens:
            if token.isdigit():
                output.append(float(token))
            elif token in precedence:
                while (operators and operators[-1] != '(' and 
                       precedence[token] <= precedence[operators[-1]]):
                    apply_operator(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators.pop())
                if operators and operators[-1] == '(':
                    operators.pop()
                else:
                    raise CalculatorError("Mismatched parentheses")
        
        while operators:
            apply_operator(operators.pop())
        
        if len(output) != 1:
            raise CalculatorError("Malformed expression")
        
        return output[0]

class Calculator:
    def __init__(self):
        pass

    def evaluate(self, expression):
        parser = ExpressionParser(expression)
        try:
            result = parser.parse()
            return result
        except CalculatorError as e:
            return f"Error: {e}"

def main():
    print("Simple Command-Line Calculator")
    print("Supported operations: +, -, *, /, ^ (exponentiation)")
    print("Type 'exit' to quit.")
    
    calculator = Calculator()
    
    while True:
        user_input = input("Enter expression: ")
        if user_input.lower() == 'exit':
            break
        
        result = calculator.evaluate(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
