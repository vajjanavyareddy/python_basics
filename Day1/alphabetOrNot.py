def alpha(c):
    if(c>='A' and c<='Z' or c>='a' and c<='z'):
        return "alphabet"
    else:
        return "not a alphabet"
cha = input("ENter character: ")
print("Given character is ",alpha(cha))