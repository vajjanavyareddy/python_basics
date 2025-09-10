li = []
n = int(input("Enter number of elements: "))
for i in range(1, n+1):
    ele = int(input(f"Enter element {i}: "))
    li.append(ele)

even_count = 0
odd_count = 0

for num in li:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
