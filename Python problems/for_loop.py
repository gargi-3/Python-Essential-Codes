# For Loop + Range function
# for i in range(0,10+1,1):
#     print(i)

# For loop another example
# start = int(input("Enter value for start: "))
# stop = int(input("Enter value for stop: "))
# step = int(input("Enter value for step: "))

# for i in range(start,stop+1,step):
#     print("Hello All!",i)

# Print summation of first-n numbers
# n = int(input("Enter value for n: ")) # n = 10 -> 1+2+3+4+5+6+7+8+9+10 = 55
# sum = 0

# for i in range(1,n+1,1):
#     sum += i

# print("Summation:",sum)

# Print table of a given number. Take the number from user.
# num = 5 --> 5 * 1 = 5
# n = int(input("Enter value for n: "))

# for i in range(1,10+1,1):
#     print(n,"*",i,"=",(n*i))

# Print the even numbers till 50.
# for i in range(0,50+1,1):
#     if(i%2 == 0):
#         print(i)

# Print the factorial of a given number.
# num = 5 => 5*4*3*2*1

num = int(input("Enter value for num: "))
fact = 1

for i in range(1,num+1,1):
    fact *= i

print("Factorial of given no.:",fact)