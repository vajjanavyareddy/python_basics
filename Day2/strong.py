def strong(n):
    org = n
    sum=0
    while(n>0):
        rem=n%10
        sum=sum+fact(rem)
        n=n//10
    if sum==org:
        return True
    else:
        return False
def fact(n):
    i=1
    f=1
    while(i<=n):
        f=f*i
        i=i+1
    return f
n = int(input("Enter range: "))
for i in range(1,n+1):
    if strong(i)==True:
        print(i)
