iamount = float(input("Enter the money amount: "))

if(iamount>=10000):
    interestRate=0.07
elif(iamount<10000):
    interestRate=0.05
    
interest = iamount * interestRate
tax = 0.02 * interest
famount = iamount + interest - tax
print(famount,"is the total money after one year")