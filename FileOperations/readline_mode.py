file = open("file1.txt","r")
data = file.readline() # reads single line, the first one
print(data)
file.close()

file = open("file1.txt","r") # reads all the lines in file but stores them in list format
data = file.readlines()
print(data)
file.close()