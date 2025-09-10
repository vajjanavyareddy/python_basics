str = input("Enter string: ")
vowels = ['a','e','i','o','u']
v =0
co=0
def count(str):
    global v,co
    for c in str:
        if c in vowels:
            v+=1
        else:
            co+=1
count(str)
print("Count of vowels: ",v)
print("Count of consonants: ",co)