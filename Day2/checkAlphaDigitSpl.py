def check(c):
    if(c>='a' and c<='z'  ):
        return "small alphabet"
    elif c>='A' and c<='Z':
        return "Big alphabet"
    elif c >='0' and c<='9':
        return "digit"
    else:
        return "special character"
ch = input("Enter character: ")
print("Character is a ",check(ch))