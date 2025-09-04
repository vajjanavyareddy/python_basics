def armstrong(num):
    org=num
    sum=0
    while(num>0):
        rem= num%10
        sum=sum+rem**3
        num=num//10
    if sum==org:
        return True
    else:
        return False
num = int(input("Enter range: "))
# print(armstrong(num))
for i in range(1,num+1):
    if armstrong(i)==True:
        print(i)

        