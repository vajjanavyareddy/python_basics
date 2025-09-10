li = []
n = int(input("Enter number of elements: "))
for i in range(1, n+1):
    ele = int(input(f"Enter ele {i}: "))
    li.append(ele)

neglist = []
for ele in li:
    if ele < 0:
        neglist.append(ele)

print("The list elements are: ", li)
print("The negative elements are: ", neglist)
