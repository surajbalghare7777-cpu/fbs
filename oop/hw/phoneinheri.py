class phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand
    def set_brand(self, Nbrand):
        self.brand = Nbrand

    def get_model(self):
        return self.model
    def set_model(self, Nmodel):
        self.model = Nmodel

    def display_info(self):
        print(f"Brand: {self.get_brand()}, Model: {self.get_model()}")

class smartphone(phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def get_os(self):
        return self.os
    def set_os(self, Nos):
        self.os = Nos

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.get_os()}")