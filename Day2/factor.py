def factor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
n = int(input("Enter number: "))
factor(n)