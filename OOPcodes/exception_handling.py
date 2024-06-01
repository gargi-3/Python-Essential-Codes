def divide(num,den):
    try:
        result = num / den
    except ZeroDivisionError:
        print("Error:Cannot divide by 0")
    except TypeError as d:
        print(f"Error:{d}")
    else:
        print("Result of division:",result)
    finally:
        print("Closing the resources opened.")

divide(20,2)
divide(10,0)
divide(24,4)
divide(30,10)
divide(20,'b')