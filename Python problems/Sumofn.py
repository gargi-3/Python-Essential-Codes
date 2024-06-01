#Sum of n natural numbers using while loop
n=int((input("Enter the no.: ")))
i=1
sum=0

while(i<=n):
    sum=sum+i
    i=i+1

print("Sum of n natural numbers is",int(sum))