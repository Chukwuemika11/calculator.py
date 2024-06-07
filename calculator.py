def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
   return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = float(input(f"input your first number:"))    
num2 = float(input(f"input your second number:"))   

for symbols in operations:
    print(symbols)

operation_symbol = input("input a symbol listed above")

calculated_operations = operations[operation_symbol]

answer = calculated_operations(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")