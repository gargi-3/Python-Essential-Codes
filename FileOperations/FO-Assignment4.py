# Consider the file test.txt and perform following operations
# 1. open the file if exists, if not create a new file
file = open("test.txt","a+")

# 2. add string 'abcde' to the end of the file
file.write('abcde')

# 3. read and display first 5 characters
file.seek(0)  # Move the file pointer to the beginning
data = file.read(5)
print("Result:",data)

# 4. display total number of characters present in the file
file.seek(0)
totalChar = len(file.read())
print("Total number of characters in the file:",totalChar)
