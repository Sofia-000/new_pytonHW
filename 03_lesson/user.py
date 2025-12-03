class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_firstName(self):
        print("Только имя ", self.first_name)

    def say_lastName(self):
        print("Только фамилия ", self.last_name)

    def say_first_last_name(self):
        print("Имя и фамилия ", self.first_name, self.last_name)


alex = User("Alexander", "Ivanov")
alex.say_firstName()
alex.say_lastName()
alex.say_first_last_name()
