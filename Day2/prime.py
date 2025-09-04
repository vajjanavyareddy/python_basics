def prime(n):
    if n==1:
        return "not prime"
    i=2
    c=0
    while(i<=n):
        if n %i==0:
            c=c+1
        i=i+1
    if c>1:
        return "not prime"
    else:
        return "prime"
n = int(input("ENter number: "))
print("Number is ",prime(n))