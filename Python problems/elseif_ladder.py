# Else if
num = int(input("Enter value for num:"))
if num % 3 == 0 and num % 5 == 0:
    print(num,"is divisible by 3 and 5 both.")
elif num % 3 == 0:
    print(num,"is divisible by 3 only.")
elif num % 5 == 0:
    print(num,"is divisible by 5 only.")
else:
    print(num,"is neither divisible by 3 nor by 5.")