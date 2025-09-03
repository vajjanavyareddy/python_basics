def largest(num1,num2,num3):
    if num1 > num2 and num2 > num3:
        return num1
    else:
        if num2>num3:
            return num2
        else:
            return num3
a = int(input("ENter a: "))
b = int(input("ENter b: "))
c = int(input("ENter c: "))
print("Largest number is: ",largest(a,b,c))
