def fAndL(num):
    last = num%10
    first =0
    while(num>0):
        rem = num%10
        first = num
        num=num//10
    return first+last
n = int(input("Enter number: "))
print("Sum of first and last digit: ",fAndL(n))