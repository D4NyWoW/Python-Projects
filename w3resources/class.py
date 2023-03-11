# create an instance of a specified class and display the namespace of the said instance
class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name
student = Student('1', 'Dick Grayson', 'Martial Arts')
#print(student.__dict__)

# Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

school_bus = Bus("School Volvo", 180, 12)
print(school_bus.seating_capacity())

