from math import pi

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
book1 = Book("название", "автор", "год")
print(book1.get_info())

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_perimeter(self):
        return pi*2*self.radius
circle1 = Circle(6)
print(circle1.get_radius())
circle1.set_radius(8)
print(circle1.get_radius())
print(circle1.get_perimeter())
