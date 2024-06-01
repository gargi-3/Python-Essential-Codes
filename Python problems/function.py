# Functions

# Function with no parameters and no return value
# def addition():
#     num1 = int(input("Enter value for num1: "))
#     num2 = int(input("Enter value for num2: "))
#     result = num1 + num2
#     print("Result of Addition:",result)
# addition()

# Function with parameters but no return value
# def subtraction(x,y):
#     result = x - y
#     print("Result of Subtraction:",result)
# x = int(input("Enter value for x: "))
# y = int(input("Enter value for y: "))
# subtraction(x,y)

# Function with no parameters but return value
# def division():
#     n1 = int(input("Enter value for n1: "))
#     n2 = int(input("Enter value for n2: "))
#     result = n1 // n2
#     return result
# tempResult = division()
# print("Result of division:",tempResult)

# Function with parameters and return value
# def multiplication(a,b):
#     return a * b
# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))
# tempResult = multiplication(a,b)
# print("Result of multiplication:",tempResult)

# Create following functions : 
# 1. Swapping two numbers without third variable
def swap():
    num1 = int(input("Enter value for num1: "))
    num2 = int(input("Enter value for num2: "))
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("After swapping: num1=",num1,"& num2=",num2)
swap()

# 2. Area of triangle
def area(b,h):
    result = 0.5 * b * h
    print("Area of triangle:",result)
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
area(b,h)

# 3. Factorial of a number
def factorial():
    term = int(input("Enter the value: "))
    x=1
    fact=1 
    while(x<=term): 
        fact=fact*x 
        x=x+1
    return fact
print("Factorial:",factorial())

# 4. Summation of first n numbers
def summation(n):
    i=1
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum
n=int((input("Enter the no.: ")))
print("Summation:",summation(n))