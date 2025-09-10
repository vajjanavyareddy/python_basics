set = set()
def adding(n):
    i=0
    while(i<=n):
        ele = int(input("Enter ele: "))
        set.add(ele)
        i+=1
n = int(input("Enter no. of ele: "))
adding(n)
print(set)