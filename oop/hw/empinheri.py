class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        return self.name
    def set_name(self, Nname):
        self.name = Nname

    def get_age(self):
        return self.age
    def set_age(self, Nage):
        self.age = Nage

    def get_salary(self):
        return self.salary
    def set_salary(self, Nsalary):
        self.salary = Nsalary

    def display(self):
        print(f"Name: {self.get_name()}, Age: {self.get_age()}, Salary: {self.get_salary()}")

class hr(employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def get_department(self):
        return self.department
    def set_department(self, Ndepartment):
        self.department = Ndepartment

    def display(self):
        super().display()
        print(f"Department: {self.get_department()}")

e1 = employee("suraj", 30, 50000)
e1.display()

e2 = hr("priya", 25, 60000, "IT")
e2.display()