# Write a program using functions to Compute the monthly payment, 
# given the loan amount, number of years and the annual interest rate.

# def monthly_pay(loan_amt,no_of_yrs,interest_rate):
#     no_of_months = no_of_yrs * 12
#     monthly_ir = interest_rate/12/100

#     # MP = (I*L) / (1-(1+I)^(-n))
#     monthly_payment = (monthly_ir*loan_amt) / (1-(1+monthly_ir)**(-no_of_months))
#     return monthly_payment
# loan_amt = float(input("Enter the Loan amount: "))
# no_of_yrs = int(input("Enter the No. of years: "))
# interest_rate = int(input("Enter the Annual interest rate: "))
# print("Monthly Payment:",monthly_pay(loan_amt,no_of_yrs,interest_rate))

# Write a program using function definition to print multiplication 
# of all the numbers in a list.
def multiplication(num):
    result = 1
    for n in num:
        result *= n
    return result
num = []
for i in range(6):
    n = int(input("Enter the number: "))
    num.append(n)
print("Given list:",num)
print("Product:",multiplication(num))