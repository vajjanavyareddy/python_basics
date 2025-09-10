li=[2,4,5,6,1,3]
index = int(input("Enter index: "))

li2 = li[:index]+li[index+1:]
print("Updated list: ",li2)