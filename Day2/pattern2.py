def pattern():
    for i in range(1,5+1):
        for j in range(1,5+1):
            if(i==j ):
                print("$",sep=" ",end =" ")
            else:
                print("*",sep=" ",end=" ")
        print(" ")
pattern()