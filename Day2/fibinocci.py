def fibinocci(n):
    a =0
    b=1
    
    print(a,end=" ")
    print(b,end=" ")
    while(a<n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
n=int(input("Enter n: "))
fibinocci(n)