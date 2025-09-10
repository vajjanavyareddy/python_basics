li=[1,2,3,4,5,6,7,4,3,2,5,6]

fr={}
for num in li:
    fr[num]=fr.get(num,0)+1
sum=0
for c in fr.values():
    if c>1:
        sum+=(c-1)
print("Count of dupliactes: ",sum)
print("Unique elemnets are: ")
for num in fr:
    if fr[num]==1:
        print(num)
        
