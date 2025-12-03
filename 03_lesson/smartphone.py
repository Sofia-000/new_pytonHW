class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def say_brand(self):
        return self.brand

    def say_model(self):
        return self.model

    def say_number(self):
        return self.number
