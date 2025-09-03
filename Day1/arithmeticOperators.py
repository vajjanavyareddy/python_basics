def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
def floor(num1,num2):
    return num1//num2
def pow(num1,num2):
    return num1**num2

def arithmetic(x,y):
    print("Addition: ",add(x,y))
    print("Subtraction: ",sub(x,y))
    print("Multiplication: ",mul(x,y))
    print("Division: ",div(x,y))
    print("Modulus: ",mod(x,y))
    print("Floor Division: ",floor(x,y))
    print("Exponent: ",pow(x,y))
number1 = int(input("ENter number1: "))
number2 = int(input("ENter number2: "))
arithmetic(number1,number2)