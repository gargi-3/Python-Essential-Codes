# We will use the calculator_module to perform maths operations
import calculator_module

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

result = calculator_module.addition(a,b)
print("Addition:",result)

result = calculator_module.subtraction(a,b)
print("Subtraction:",result)

result = calculator_module.division(a,b)
print("Division:",result)