# Lock: acquire and release
from threading import Thread, Lock


class Counter(Thread):
    tickets=30
    def __init__(self,nm=""):
        super(Counter, self).__init__()
        self.name=nm
    def __add__(self, other):
        if other<=self.tickets:
            owe=other*120
            fare=int(input("Pay your amount to get the tickets: "))
            if fare>=owe:
                self.tickets-=other
                print(other,"tickets has booked for",self.name)
                return True
            else:
                print(other,"tickets cannot be booked for",self.name)
                return False
        else:
            print(other,"number of tickets not available")
            return False
    def run(self):
        hold.acquire()
        tick=int(input("Tell us no of ticket's you want:"+self.name))
        self+tick
        hold.release()
        print("Thanks for reaching US")

hold=Lock()

a=Counter("Sasi")
b=Counter("Dinesh")
c=Counter("Vinay")
d=Counter("Vignesh")

a.start()
b.start()
c.start()
d.start()


