def prime(n):
    if n==1:
        return False
    i=2
    c=0
    while(i<=n):
        if n %i==0:
            c=c+1
        i=i+1
    if c>1:
        return False
    else:
        return True

def factor(num):
    for i in range(1,num+1):
        if num%i==0 and prime(i)==True:
            print(i)
n = int(input("Enter number: "))
factor(n)