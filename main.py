from abc import ABC,abstractmethod
class Vehicle (ABC):
    @abstractmethod
    def calculate_rent():
        pass

class Car(Vehicle):
    def calculate_rent(self):
        return ("Car Rental: $150")
class Bike(Vehicle):
    def calculate_rent(self):
        return ("Bike Rental: $45")
class Bus(Vehicle):
    def calculate_rent(self):
        return ("Bus Rental: 300")

Vehicle =[]
Vehicle.append(Car())
Vehicle.append(Bike())
Vehicle.append(Bus())

for v in Vehicle:
    print(v.calculate_rent())


#Practice Question 2
from abc import ABC,abstractmethod
class Student(ABC):
    def __init__ (self,assignment,final_exam):
        self.assignment = assignment
        self.final_exam = final_exam

    @abstractmethod
    def final_marks(self):
        pass

class UndergraduateStudent(Student):
    def final_marks(self):
        return (self.assignment*0.4 + self.final_exam*0.6)

class PostgraduateStudent(Student):
    def final_marks(self):
        return (self.assignment*0.3 + self.final_exam*0.7)

students =[]
students.append(UndergraduateStudent(80,70))
students.append(PostgraduateStudent(90,80))

for student in students:
    print(student.final_marks())





