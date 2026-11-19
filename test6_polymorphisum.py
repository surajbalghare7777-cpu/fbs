from abc import ABC, abstractmethod


class Vehicle(ABC):                    
    def __init__(self, number, persons):
        self.number = number
        self.persons = persons

    def getNumber(self):
        return self.number

    def setNumber(self, newNumber):
        self.number = newNumber

    def getPersons(self):
        return self.persons

    def setPersons(self, newPersons):
        self.persons = newPersons

    def __str__(self):
        return f"Number={self.number} persons={self.persons}"

    def display(self):
        print(self)

    @abstractmethod
    def calToll(self):
        pass


class TwoWheeler(Vehicle):
    def calToll(self):
        extra = (self.persons - 2) * 10 if self.persons > 2 else 0
        print(f"Toll of Two Wheeler= {20 + extra}")


class ThreeWheeler(Vehicle):
    def calToll(self):
        extra = (self.persons - 3) * 20 if self.persons > 3 else 0
        print(f"Toll of Three Wheeler= {30 + extra}")


class FourWheeler(Vehicle):
    def calToll(self):
        extra = (self.persons - 4) * 40 if self.persons > 4 else 0
        print(f"Toll of Four Wheeler= {40 + extra}")


class HeavyVehicle(Vehicle):
    def __init__(self, number, persons, wheels):
        super().__init__(number, persons)
        self.wheels = wheels

    def getWheels(self):
        return self.wheels

    def setWheels(self, newWheels):
        self.wheels = newWheels

    def display(self):
        super().display()
        print(f"Wheels= {self.wheels}")

    def calToll(self):
        extra = (self.persons - 6) * 100 if self.persons > 6 else 0
        print(f"Toll of Heavy Vehicle= {60 + extra}")




# b = TwoWheeler("MH12AA11111", 3)
# c = FourWheeler("MH14BB2222", 6)
# t = HeavyVehicle("MH15CC3333", 8, 6)

# for veh in (b, c, t):             
#     veh.display()
#     veh.calToll()


while True:
    print("\n1. Two Wheeler\n2. Three Wheeler\n3. Four Wheeler\n4. Heavy Vehicle\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 5:
        break
    if choice not in (1, 2, 3, 4):
        print("Invalid choice")
        continue

    number = input("Vehicle number: ")
    persons = int(input("Number of persons: "))

    if choice == 1:
        veh = TwoWheeler(number, persons)
    elif choice == 2:
        veh = ThreeWheeler(number, persons)
    elif choice == 3:
        veh = FourWheeler(number, persons)
    else:
        wheels = int(input("Number of wheels (more than 4): "))
        veh = HeavyVehicle(number, persons, wheels)

    veh.display()
    veh.calToll()                    