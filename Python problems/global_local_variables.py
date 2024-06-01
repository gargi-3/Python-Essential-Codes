# Global and Local variables
result = 10 #global var

def add(a,b):
    result1 = result + a + b
    return result1

def display():
    x = 100 #local var
    print("Initial result:",result)
    sum = result + x
    print("Result after adding x:",sum)

temp = add(10,10)
print("Temp:",temp)

display()