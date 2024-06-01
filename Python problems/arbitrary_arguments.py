# Arbitrary argument functions
def total(*args):
    sum = 0
    for i in args:
        sum += i
    print("Summation:",sum)

total(1,2,3,4,5,6,7,8,9,10)
total(100,200,300,400,500)