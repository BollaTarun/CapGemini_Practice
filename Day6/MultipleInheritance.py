

# class Bird:
#     def fly(self):
#         return "This Bird can Fly."
    
# class Mammal:
#     def walk(self):
#         return "This Mammal can Walk."
    
# class Bat(Bird,Mammal):
#     pass

# bat=Bat()
# print(bat.fly())
# print(bat.walk())




class Vehicle:
    def __init__(self,type):
        self.type=type
    
class Car(Vehicle):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand=brand
    
class Electric(Car,Vehicle):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand=brand
