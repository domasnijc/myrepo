class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return(f"Имя: {self.name}, id: {self.id}")

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"
    
    def manage_project(self, project_name):
        return f"{self.name} выполняет проект {project_name}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"       
        
    def perform_maintenance(self, do_maintenance):
        if do_maintenance:
            return f"{self.name} выполняет техническое обслуживание"
        elif do_maintenance == False:
            return f"{self.name} не выполняет техническое обслуживание"
        else:
            return "Введите корректное значение"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Technician.__init__(self, name, id, specialization)
        Manager.__init__(self, name, id, department)

        self.subordinates = []  

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        print("Список подчиненных:")
        for item in self.subordinates:
            print(item.get_info())
            

employee1 = Employee("Сергей", 1)
print(employee1.get_info())
manager1 = Manager("Денис", 2, "ит")
print(manager1.get_info())
print(manager1.manage_project("project"))
technician1 = Technician("Петр", 3, "ии")
print(technician1.get_info())
print(technician1.perform_maintenance(True))
techManager1 = TechManager("Андрей", 4, "ит", "ии")
print(techManager1.get_info())
print(techManager1.manage_project("project1"))
print(techManager1.perform_maintenance(False))
techManager1.add_employee(manager1)
techManager1.add_employee(technician1)
techManager1.get_team_info()
