def sumOfDigits(num):
    sum=0
    
    while(num>0):
        rem = num%10
        sum= sum+rem
        num=num//10
        
    return sum
n = int(input("Enter number: "))
print("Sum od digits is ",sumOfDigits(n))
    