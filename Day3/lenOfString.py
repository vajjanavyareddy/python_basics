str = "hello welcome"
str1 = "hello welcome"
def length(str):
    
    ch=0
    for char in str:
        ch+=1
    print("Length: ",ch)

def compareStrings(str1,str2):
    if len(str)!=len(str1):
        return False
    for i in range(len(str)):
        if str[i]!=str1[i]:
            return False
    return True
length(str)
if(compareStrings(str,str1)):
    print("Two strings are equal")
else:
    print("Two strings are not equal")
res=""
for char in str:
    res+=char
for char in str1:
    res+=char
print("Result string: ",res)
    

