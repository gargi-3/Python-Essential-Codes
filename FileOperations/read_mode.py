#Read mode example
file = open("file1.txt","r")
data = file.read()
print("Data from File1:",data)
file.close()

file = open("file1.txt","r")
data = file.read(15)
print("Data from File1:",data)
file.close()