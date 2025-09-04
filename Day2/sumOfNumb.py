def summ(n):
    sum =0
    i=0
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum
n = int(input("ENter n value: "))
print("Sum of n numbers: ",summ(n))