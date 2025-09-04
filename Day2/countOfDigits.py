def count(n):
    c =0
    while(n>0):
        rem= n%10
        c=c+1
        n=n//10
    return c
n = int(input("Enter number: "))
print("Count of digits: ",count(n))