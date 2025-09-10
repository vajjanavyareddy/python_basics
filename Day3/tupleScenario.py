
# A school stores student records as tuples in the format (roll_no, name, marks).
# Write a Python program to:
# Store the data of 5 students in a list of tuples.
# Print the name of the student who scored the highest marks.
# Print all students who scored more than 75 marks.
n = int(input("Enter number of students: "))

li = []

for i in range(n):
    roll = int(input(f"Enter roll number for student {i+1}: "))
    name = input(f"Enter name for student {i+1}: ")
    marks = int(input(f"Enter marks for student {i+1}: "))
    li.append((roll, name, marks))
max =0
for tup in li:
    marks = tup[2]
    if marks>max:
        max = marks
        topStu_name = tup
print(f"Max marks {max} scored by {topStu_name}")
for tup in li:
    marks = tup[2]
    if tup[2]>75:
        print(tup)
