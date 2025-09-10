str = "abc2355#2!!"
alpha =0
digit=0
spl=0
def count(str):
    global alpha,digit,spl
    for c in str:
        if(c>='a' and c<='z'  ):
            alpha+=1
        elif c>='A' and c<='Z':
            alpha+=1
        elif c >='0' and c<='9':
            digit+=1
        else:
            spl+=1
count(str)
print("Alphabets: ",alpha)
print("Digits: ",digit)
print("Special characters: ",spl)
