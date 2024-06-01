# Palindrome Number

num = int(input("Enter the number: "))
temp = num
rem = 0 #Remainder
reverse = 0

while num > 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10
print("Reversed number:",reverse)

if(temp == reverse):
    print("It's a palindrome number.")
else:
    print("Not a palindrome number.")