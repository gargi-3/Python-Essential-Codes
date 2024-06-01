# List and math operations
# numbers = [10,20,30,40,50]
# result = 0
# for i in numbers:
#     result += i

# print("Summation:",result)

# in and not in are membership operators.
# print(numbers)
# print(30 in numbers)
# print(60 in numbers)
# print(40 not in numbers)

# Calculate addition of first 10 numbers and also calculate avg.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
sum = 0
avg = 1
for i in numbers[:10:1]:
    sum += i
print("Sum of first 10 numbers:",sum)
average = sum / i
print("Average of first 10 numbers:",average)