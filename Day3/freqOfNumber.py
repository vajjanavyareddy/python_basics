li = [0,1,2,3,4,5,3,2,1,3]
fr = {}
for num in li:
    if num in fr:
        fr[num]+=1
    else:
        fr[num]=1
for num in fr:
    print(num ," -> ",fr[num])