# vowels = ['a','e','i','o','u']
def check(c):
    if c =='a' or c == 'e' or c=='i' or c=='o' or c=='u':
        return "vowel"
    else:
        return "consonant"
char = input("ENter character: ")
print("Given character is ",check(char))