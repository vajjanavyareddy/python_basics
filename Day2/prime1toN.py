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
n = int(input("ENter range: "))
for i in range(1,n+1):
    if prime(i)==True:
        print(i)