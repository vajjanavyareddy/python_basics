li = [2,3,4,7,9,1]
max=float('-inf')
smax=float('-inf')

for num in li:
    if num>max:
        smax=max
        max=num
    
    elif num>smax and num!=max:
            smax=num
print("Max: ",max)
print("Smax: ",smax)