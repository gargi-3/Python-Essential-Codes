# n!= n*(n-1)*(n-2)...*1
# 5!= 5*4*3*2*1

term = int(input("Enter the value: "))
x=1
fact=1 

while(x<=term): #6<=5; 1,2,3,4,5
    fact=fact*x #1*1,1*2,2*3,6*4,24*5 #fact=120
    x=x+1

print("Factorial of",term,"is",fact)