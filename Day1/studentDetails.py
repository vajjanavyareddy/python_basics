#calculating student marks and printing details
sname = input("Enter name: \n")
sno = int(input("Enter number: \n"))
phy = int(input("Enter physics marks: "))
mat= int(input("Enter maths marks: "))
che = int(input("Enter chemistry marks: "))
totalMarks = phy+mat+che
average = totalMarks/3
print("STUDENT DETAIL")
print("Student number: ",sno)
print("Student name: ",sname)
print("Student total Marks: ",totalMarks)
print("Student Average MArks: ",round(average,2))