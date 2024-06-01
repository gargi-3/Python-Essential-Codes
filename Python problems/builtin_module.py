# Math module
import math

print(math.factorial(5))
print(math.sqrt(16))
print(math.pow(3,2))
print(math.pi)

# datetime
import datetime
date = datetime.datetime.now()
print(date)
print(date.day)
print(date.month)
year = date.strftime('%Y')
print(year,type(year))

# random module
import random
for i in range(10):
    print(random.random())

for i in range(1,10):
    print(random.randint(1,10))