n1 = int(input("Enter number-1: "))
n2 = int(input("Enter number-2: "))

try:
    div = n1/n2
except:
    raise Exception("Divisible by zero not possible")
else:
    print(f"Division performed. value is : {div}")
finally:
    print("Try some other numbers")