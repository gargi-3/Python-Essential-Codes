class Test:
    def __init__(self):
        print("Initialising object")
    
    def __del__(self):
        print("Deallocating the acquired memory")

t1 = Test()
del t1

print("Next half of the code")