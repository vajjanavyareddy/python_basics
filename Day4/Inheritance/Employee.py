class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Employee name: {self.name}")
        print(f"Employee Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept= dept
    def display(self):
        super().display()
        print(f"Department: {self.dept}")
obj1 = Manager("ram",45000,"CSE")
obj2 = Manager("raju",89000,"CDC")
print("\nEmployee-1 Details:\n")
obj1.display()
print("\nEmployee-2 details: \n")
obj2.display()
eob = Employee("raghav",56000)
print("\nEmployee details by using Employee obj\n")
eob.display()