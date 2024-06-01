# List demo

fruits = ['apple','banana','orange','kiwi','litchi','pear']
print(fruits)

city = []   # empty list
print(city)

n = 5
city = [None] * n   # size of the list
city[0] = 'nashik'
city[1] = 'mumbai'
city[2] = 'pune'
print(city)
city.insert(3,'nagar')
city.insert(4,'dhule')
city.append('kolhapur')
city.append('nagpur')
print(city)