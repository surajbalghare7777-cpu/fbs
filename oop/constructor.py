class emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
e1 = emp("Suraj", 25)
e1.display()
