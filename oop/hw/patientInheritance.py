class patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name
    def set_name(self, Nname):
        self.name = Nname       

    def get_age(self):
        return self.age
    def set_age(self, Nage):
        self.age = Nage

    def get_gender(self):
        return self.gender
    def set_gender(self, Ngender):
        self.gender = Ngender

    def display_info(self):
        print(f"Name: {self.get_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}")

class admitted_patient(patient):
    def __init__(self, name, age, gender, admission_date):
        super().__init__(name, age, gender)
        self.admission_date = admission_date

    def get_admission_date(self):
        return self.admission_date
    def set_admission_date(self, Nadmission_date):
        self.admission_date = Nadmission_date

    def display_info(self):
        super().display_info()
        print(f"Admission Date: {self.get_admission_date()}")

p1 = patient("suraj", 30, "Female")
p1.display_info()

a1 = admitted_patient("priya", 25, "Female", "2023-10-01")
a1.display_info()