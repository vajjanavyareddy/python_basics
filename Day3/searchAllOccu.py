str = input("Enter string: ")
ch = input("Enter character to search: ")
pos =[]
for c in range(len(str)):
    if str[c]==ch:
        pos.append(c)
print(pos)