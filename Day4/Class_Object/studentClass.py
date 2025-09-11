class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll= roll
        self.marks = marks
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student roll: {self.roll}")
        print(f"Student marks: {self.marks}")
stu1 = Student("abc",23,98)
stu2 = Student("xyz",24,89)
stu3 = Student("pqr",25,97)
print("\nStudent-1 Details:\n ")
stu1.display()
print("\nStudent-2 details: \n")
stu2.display()
print("\nStudent-3 details: \n")
stu3.display()
