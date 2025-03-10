
# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Bark")

# for animal in [Cat(),Dog()]:
#     animal.sound()


# class Bike:
#     def details(self):
#         print("\nBike:\n2 Wheeler Vehicle")
    
#     def gear(self):
#         print("Maual Gears")

#     def fuel(self):
#         print("Fuel : Petrol and Electric")

# class Car:
#     def details(self):
#         print("\nCar:\n4 Wheeler Vehicle")

#     def gear(self):
#         print("Manual and Automatic Gears")

#     def fuel(self):
#         print("Fuel : Diesel, Petrol and Electric")

# for vehicle in [Bike(),Car()]:
#     vehicle.details()
#     vehicle.fuel()
#     vehicle.gear()



class Employee:
    data=[]
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

    def get_age(self):
        return self.age
    
    # def collection(self):
    #     self.data.append(self.name)
    #     self.data.append(self.id)
    #     self.data.append(self.salary)
    #     return self.data

class Student:
    data=[]
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

    def get_age(self):
        return self.age


std=[]

for person in [Employee(input("Employee Details\nName:"),input("ID: "),input("Age: ")),Student(input("Student Details\nName: "),input("ID: "),input("Age: "))]:
    std.append(person.get_name())
    std.append(person.get_id())
    std.append(person.get_age())

print(std)

