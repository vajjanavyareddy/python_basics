def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j or i+j-1==n):
                print("$",sep=" ",end =" ")
            else:
                print("*",sep=" ",end=" ")
        print(" ")
n=int(input("ENter n: "))
pattern(n)