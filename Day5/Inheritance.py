
class Parent:

    def __init__(self):
        self.bigNose="7CM"

    def display_parent(self):
        print("This is a Parent Class.")
    
class Child(Parent):

    def __init__(self):
        super().__init__()

    def display_child(self):
        print("This is a Child Class.")

child=Child()
child.display_child()
child.display_parent()
print(child.bigNose)
parent=Parent()
print(parent.bigNose)




# class School:
#     def __init__(self,name,id,address):
#         self.name=name
#         self.id=id
#         self.address=address
    
#     def display(self):
#         print("Name    :",self.name)
#         print("ID      :",self.id)
#         print("Address :",self.address)


# class UG_College(School):
#     def __init__(self,branch):
#         super().__init__()
#         self.branch=branch

#     def display(self):
#         print("Branch :",self.branch)

# class PG_College(UG_College):
#     def __init__(self,domain):
#         super().__init__()
#         self.domain=domain
    
#     def display(self):
#         print("Domain : ",self.domain)

# pg=School("Raj",5,"HYD")
# pg.display()
