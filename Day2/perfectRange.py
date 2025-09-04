def perfect(n):
    org =n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if org==sum:
        return True
    else:
        return False
n=int(input("Enter range: "))
for i in range(1,n+1):
    if perfect(i)==True:
        print(i)
    