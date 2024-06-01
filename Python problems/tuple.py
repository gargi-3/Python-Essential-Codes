empty_tuple = ()
print("Empty tuple:",empty_tuple)
tupleWithOneElement = (1,)
print("Tuple with one value:",tupleWithOneElement)
tupleWithMultipleElements = (1,2,3,"hello","bye","welcome",100,700,True)
print("Tuple with multiple elements:",tupleWithMultipleElements)

# accessing elements of tuple
print(tupleWithMultipleElements[2])
print(tupleWithMultipleElements[5])
print(tupleWithMultipleElements[7])

# unpacking tuple
a, b, c, d, e, f, g, h, i = tupleWithMultipleElements
print(a, b, c, d, e, f, g, h, i)

# try to modify the tuple element bye to exit
# tupleWithMultipleElements[4] = "exit"
# error : TypeError: 'tuple' object does not support item assignment (modification not allowed in tupple)

# Tuple concatenation
my_tuple1 = (10, 20, 30)
my_tuple2 = ("mumbai", "400072", "maharashtra")
new_tuple = my_tuple1 + my_tuple2
print("Concatenated tuple:",new_tuple)

# finding length of tuple
print("Length of new_tuple:",len(new_tuple))

# indexing
print(new_tuple[3])
print(new_tuple[-5])

# index() and count()
tuple1 = (10, 20, 30, 20, 30, 10, 90)
n = tuple1.count(20)
print("Count is n:",n)

i = tuple1.index(20)
print("Index value:",i)
