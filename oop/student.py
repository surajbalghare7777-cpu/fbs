class student:
    sCount=0
    def __init__(self, name, rollno, batchname):
        self.name = name
        self.rollno = rollno
        self.batchname = batchname
        student.sCount += 1

    def get_name(self):
        return self.name
    def set_name(self, Nname):
        self.name = Nname

    def get_rollno(self):
        return self.rollno
    def set_rollno(self, Nrollno):
        self.rollno = Nrollno

    def get_batchname(self):
        return self.batchname
    def set_batchname(self, Nbatchname):
        self.batchname = Nbatchname
    def display(self):
        print(f"student info:: name={self.get_name()}, rollno={self.get_rollno()}, batchyear={self.get_batchname()}")



class placedstudent(student):
    def __init__(self, name, rollno, batchname, companyname):
        super().__init__(name, rollno,batchname)
        self.companyname = companyname

    def get_companyname(self):
        return self.companyname
    def set_companyname(self, Ncompanyname):
        self.companyname = Ncompanyname

    def display(self):
        super().display()
        print(f"company_name={self.companyname}")
        print(super().sCount)

sn1=student("suraj", 101, "2023")
sn2=placedstudent("john", 102, "2024", "Google")
sn1.display()
sn2.display()