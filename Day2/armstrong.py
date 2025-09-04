def armstrong(num):
    org=num
    sum=0
    while(num>0):
        rem= num%10
        sum=sum+rem**3
        num=num//10
    if sum==org:
        return "armstrong number"
    else:
        return "not a armstrong number"
num = int(input("Enter number: "))
print(armstrong(num))
        