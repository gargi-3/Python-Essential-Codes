# nested loop

# for row in range(1,4,1):
#     print(row,end="-> ")
#     for col in range(1,5,1):
#         print(col * 2,end=" ")
#     print()   #()->prints in new line 

# task on nested loops : 

# 		1-> a b c d 
# 		2-> a b c d
# 		3-> a b c d

for row in range(1,4,1):
    print(row,end="-> ")
    for col in range(97,101,1):
        print(chr(col),end=" ")
    print()
