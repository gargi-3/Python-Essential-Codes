# Calculate factorial using recursive function
# 5! => 5*4*3*2*1 = 120

def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num-1))
    
number = int(input("Enter the value: "))
temp = factorial(number)

print("Factorial of",number,"is",temp)