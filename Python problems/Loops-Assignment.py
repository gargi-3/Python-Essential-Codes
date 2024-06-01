# Write a program that uses a while loop to add up all the even numbers 
# between 100 and 200.

# i = 100
# sum = 0
# while i<=200: 
#     if i%2 == 0: 
#         sum += i 
#     i += 1
# print("Summation:",sum)

# Write a program that receives 3 sets of values
# of p, n, and r and calculates simple interest for each.

# for i in range(3):
#     p = int(input("Enter the Principal Amount: "))
#     n = int(input("Enter the No. of Years: "))
#     r = int(input("Enter the Rate of Interest: "))

#     simple_interest = (p*n*r) / 100
#     print("Simple Interest:",simple_interest)

# Write a program to display the following pattern using nested loops.
"""
1                                                                  
22                                                             
333                                                       
4444                                                    
55555
"""

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()