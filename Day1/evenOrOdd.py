def evenOrOdd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num = int(input("Enter number: "))
print("Number is: ",evenOrOdd(num))