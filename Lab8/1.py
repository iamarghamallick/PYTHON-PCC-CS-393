# Implement a module for creating simple calculator consisting of addition, subtraction, division, and multiplication operations and import the module into another program.

import calculator

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

res_add = calculator.add(n1, n2)
res_sub = calculator.subtract(n1, n2)
res_mul = calculator.multiply(n1, n2)
res_div = calculator.divide(n1, n2)

print(f"{n1} + {n2} = {res_add}")
print(f"{n1} - {n2} = {res_sub}")
print(f"{n1} * {n2} = {res_mul}")
print(f"{n1} / {n2} = {res_div}")