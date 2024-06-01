# Copy content from one file and paste in another file 
# using file functions

file1 = open("first.txt","r")
data = file1.read()
print("Data from the first file:",data)

file2 = open("second.txt","w")
for line in data:
    file2.write(line)

file1.close()
file2.close()