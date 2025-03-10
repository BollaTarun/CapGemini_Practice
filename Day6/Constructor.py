
class Example:
    def __init__(self,a):
        print("1st Constructor : ",a)

    def __init__(self,b):
        print("2nd Constructor : ",b)

c=Example(2)  # Overrides the 1st Constructor

class Arguments:
    def __init__(self, *args):
        if len(args)==1:
            print("1 Argument :\nHello",args[0])
        elif len(args)==2:
            print("2 Arguments :\nHello",args[0],", you are",args[1],"years old.")

k=Arguments("Hari")
m=Arguments("Hari",34)
    
class Student:
    def __init__(self,studentName,**kwargs):
        self.name=studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old.")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield=kwargs['name']
    
obj1=Student(name="Hari",studentName='k')
obj2=Student(name="Hari", age=20, studentName='k')
print(obj2.xfield)



class Destructor:
    def __init__(self,name):
        self.name=name
        print(f"Object {self.name} is Constructed")
    
    def __del__(self):
        print(f"Object {self.name} is Destroyed")

obj=Destructor("Raj")
del obj