
from abc import ABC, abstractmethod

class Mail(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Mail):
    def send(self):
        print("Sending Email...")
    
    def sender(self):
        print("\nEntering the credentials of the Receiver...")

class Whatsapp(Mail):
    def send(self):
        print("Sending Message on Whatsapp...")

    def sender(self):
        print("Typing the Message to the Receiver...")

class SMS(Mail):
    def send(self):
        print("Sending SMS...")
    
    def sender(self):
        print("Typing Message to the Receiver...")

e=Email()
w=Whatsapp()
s=SMS()
e.sender()
e.send()
w.sender()
w.send()
s.sender()
s.send()
