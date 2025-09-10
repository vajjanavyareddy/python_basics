str1= input("ENter string: ")
res =""
visit = set()
for char in str1:
    if char not in visit:
        count = str1.count(char)
        res+= char + str(count)
        visit.add(char)
print(res)