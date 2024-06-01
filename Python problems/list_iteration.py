# List Iterations

fruits = ['apple','banana','orange','kiwi','litchi','pear']
print(fruits)

print(fruits[1],":",fruits[3])

print(fruits[::])
print(fruits[1:5:1])
print(fruits[1:6:2])

print(id(fruits))
fruits[3] = "papaya"
print(fruits,":",id(fruits))

for i in fruits:
    print(i)

for i in fruits:
    print(i.upper())