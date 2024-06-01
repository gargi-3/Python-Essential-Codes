# Write a program that accepts a string from the user and display the 
# same string after removing vowels from it.

# x = input("Enter the string value: ")
# vowels = "aeiou"
# new_string = ""

# for char in x:
#     if char not in vowels:
#         new_string += char
# print("String without vowels:",new_string)

# Write a program that creates a list of 10 random integers. 
# Then create two lists by name odd_list and even_list that have 
# all odd and even values of the list respectively.

# random_list = []
# odd_list = []
# even_list = []

# for i in range(10):
#     n = int(input("Enter any random integer: "))
#     random_list.append(n)
# print("Given list values:",random_list)

# for i in random_list:
#     if i%2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# print("Even values of given list:",even_list)
# print("Odd values of given list:",odd_list)

# Write a program that has the dictionary of your friends’ names as keys 
# and phone numbers as its values. Print the dictionary in a sorted order. 
# Prompt the user to enter the name and check if it is present in the dictionary. 
# If the name is not present,then enter the details in the dictionary.

friends = {'Misa':9876543211,'Vasu':9897654326,'Carol':8102675343}

print("Friends Dictionary->")
for name in sorted(friends.keys()):
    print("{}: {}".format(name,friends[name])) 

name = input("Enter the name of your friend: ")
if name.capitalize() in friends:
    print("{} is there in your friends dictionary.".format(name))
else:
    print("""{} is not there in your friends dictionary :(
          Aww, add up asap!!!""".format(name))
    friends[name.capitalize()] = int(input("Enter friend's number: "))

print("Updated Friends Dictionary->")
for name in sorted(friends.keys()):
    print("{}: {}".format(name,friends[name]))