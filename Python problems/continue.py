# using continue in even-odd logic 
# and for every odd we will skip the logic

for i in range(1,10+1):
    if i % 2 != 0:
        continue
    print(i)