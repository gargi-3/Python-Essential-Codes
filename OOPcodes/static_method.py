class StaticMethodDemo:
    @staticmethod   # denotes the underlying method as of static type
    def add(x,y):
        print("Addition:",(x+y))

"""smd = StaticMethodDemo()
smd.add(10,5)"""

StaticMethodDemo.add(15,5)  # standard way of invoking a classname