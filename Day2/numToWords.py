def convert(num):
    num = reversed(num)
    while(num>0):
        rem=num%10
        num=num//10
        print(value(rem),sep=" ",end=" ")
        
def value(n):
    if n==1:
        # print("one")
        return "one"
    elif n==2:
        return "two"
        # print("two")
    elif n==3:
        return "three"
    elif n==4:
        return "four"
    elif n==5:
        return "five"
        # print("five")
    elif n==6:
        return "six"
        # print("six")
    elif n==7:
        return "seven"
        # print("seven")
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    else:
        return "zero"
def reversed(num):
    rev = 0
    while(num>0):
        rem = num%10
        rev=rev*10+rem
        num=num//10
    return rev
n = int(input("ENter number: "))
convert(n)