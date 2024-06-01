# Swapping two numbers using a temporary variable
# num1 = int(input("Enter 1st value: "))
# num2 = int(input("Enter 2nd value: "))

# temp = num1
# num1 = num2
# num2 = temp

# print("Num1 value:",num1)
# print("Num2 value:",num2)

# Swapping without using a temporary variable
num1 = int(input("Enter 1st value: "))
num2 = int(input("Enter 2nd value: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping: num1 =",num1,"num2 =",num2)
