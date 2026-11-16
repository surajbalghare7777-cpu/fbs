class car:
    def __init__(self, cName, cNumber, year):
        self.cname = cName
        self.cNumber = cNumber
        self.year = year

    def get_cName(self):    
        return self.cName
    def set_cName(self, Ncname):
        self.cName = Ncname

    def get_cNumber(self):
        return self.cNumber
    def set_cNumber(self, NcNumber):
        self.cNumber = NcNumber

    def get_year(self):
        return self.year
    def set_year(self, Nyear):
        self.year = Nyear

    def display_info(self):
        print(f"Car Name: {self.get_cName()}, Car Number: {self.get_cNumber()}, Year: {self.get_year()}")

class carowner(car):
    def __init__(self, cName, cNumber, year, ownerName):
        super().__init__(cName, cNumber, year)
        self.ownerName = ownerName

    def get_ownerName(self):
        return self.ownerName
    def set_ownerName(self, NownerName):
        self.ownerName = NownerName

    def display_info(self):
        print(f"Car Name: {self.get_cName()}, Car Number: {self.get_cNumber()}, Year: {self.get_year()}, Owner Name: {self.get_ownerName()}")

c1 = car("Toyota", "ABC123", 2020)
c1.display_info()

c2 = carowner("Honda", "XYZ789", 2021, "Suraj")
c2.display_info()