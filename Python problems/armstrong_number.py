num = int(input("Enter the number: "))
n = num
rem = 0
armstrong = 0
while num > 0:
    rem = num % 10
    armstrong += rem * rem * rem
    num = num // 10

print("Armstrong value:",armstrong)
if(n == armstrong):
    print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")