ws = int(input("Enter wind speed in mph: "))

if(ws<25):
    print("Not a strong wind")
elif(ws>=25) and (ws<39):
    print("Strong wind")
elif(ws>=39) and (ws<55):
    print("Gale")
elif(ws>=55) and (ws<=72):
    print("Whole Gale")
elif(ws>72):
    print("Hurricane")