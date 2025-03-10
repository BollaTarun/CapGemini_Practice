
import threading

class BookTickets:

    def __init__(self,tickets_available):
        self.tickets_available=tickets_available
        self.lock=threading.Lock()

    def book_tickets(self,name):
        with self.lock:
            if self.tickets_available>0:
                self.tickets_available-=1
                print(f"{name}'s Ticket has booked successfully!!")
            else:
                print(f"Sorry {name}, no tickets aailable.")

b=BookTickets(1)

user=['Alice','Bob']
threads=[]

for i in user:
    thread=threading.Thread(target=b.book_tickets,args=(i,))
    #thread.start()
    threads.append(thread)

for i in threads:
    print()
