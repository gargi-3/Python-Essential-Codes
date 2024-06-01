set1 = {}
set2 = {1, 2, 3}
print("Set1:",set1)
print("Set2:",set2)

# set can be created using constructors
myset1 = set(range(1, 5))
print("Initial myset1:",myset1)
myset1.add(10)
myset1.add(20)
myset1.add(30)
myset1.add(40)
print("Myset1:",myset1)

myset1.remove(40)
print("Myset1 after removing 40:",myset1)

myset1.clear()
print("Myset1 after clear:",myset1)

# set operations
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 2, 8}

result = set1.union(set2)
print("Result after union:",result)

result = set1.intersection(set2)
print("Result after intersection:",result)