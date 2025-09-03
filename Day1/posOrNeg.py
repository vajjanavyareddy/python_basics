def check(num):
    if num==0:
        return "neither pos nor neg"
    elif num>0:
        return "positive"
    else:
        return "negative"
num = int(input("Enter number: "))
print("Number is ",check(num))