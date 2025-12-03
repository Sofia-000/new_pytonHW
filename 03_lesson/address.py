class Address:
    def __init__(self, index, sity, street, building, apartment):
        self.index = index
        self.sity = sity
        self.street = street
        self.building = building
        self.apartment = apartment

    def say_index(self):
        return self.index

    def say_sity(self):
        return self.sity

    def say_street(self):
        return self.street

    def say_building(self):
        return self.building

    def say_apartment(self):
        return self.apartment
