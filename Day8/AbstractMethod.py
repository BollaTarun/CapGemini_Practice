from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def display(self):
        pass

class Child(Father):
    def display(self):
        print("Child Class")

class Relative(Father):
    def display(self):
        print("Relative Class")

r=Relative()
c=Child()
c.display()