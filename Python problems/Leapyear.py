# Leap year or not
# Nested if
x = int(input("Enter the year: "))
if(x%4==0):
    if(x%100!=0) or (x%400==0):
        print("It is a leap year")
else:
    print("It is not a leap year")

# If else
# x = int(input("Enter the year: "))
# if(x%400==0) and (x%4==0):
#     print("It's a leap year!")
# else:
#     print("It's not a leap year!")

