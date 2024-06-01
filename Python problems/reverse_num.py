# Reverse of a number

num = int(input("Enter the number: "))
rem = 0 #Remainder
reverse = 0

while num > 0:
    rem = num % 10  #decompose number
    # print("Remainder:",rem)
    reverse = reverse * 10 + rem    #recompose reversed bits
    num = num // 10
    # print("Number:",num,"=> Reversed number:",reverse)
print("Reversed number:",reverse)