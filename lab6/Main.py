#Задание 1
class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        hashed_password = f(password)
        self.__password = hashed_password

    def set_password(self, new_pass):
        self.__password = new_pass

    def check_password(self, password):
        hashed_password = f()
        if self.__password == password:
            return True
        else:
            return False

user1 = UserAccount("name", "email", "password")
user1.set_password("password2")
print(user1.check_password("password2"))

#Задание 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"
    
vehicle1 = Vehicle("Make", "Model")
print(vehicle1.get_info())

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f"{super().get_info()}, Тип топлива: {self.fuel_type}"

car1 = Car("Make", "Model", "Fuel_type")
print(car1.get_info())