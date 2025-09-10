li=[1,3,4,3,2,1]
fr={}
for num in li:
    fr[num]=fr.get(num,0)+1
for num in fr:
    if fr[num]==1:
        print(num)
