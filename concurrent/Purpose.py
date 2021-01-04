#multithread basic sample
from threading import Thread

# resource class
class Alpha(Thread):
    def __init__(self,nm=""):
        super(Alpha, self).__init__()
        self.name=nm
        self.rec=[56,12,45,99,11,9,4,1,8,5,41,9,20,0,6,32]
    def run(self):
        print(self.name,"came inside")
        for x in self.rec:print(x)

a=Alpha("Albert")
b=Alpha("Bosker")
c=Alpha("Christy")
d=Alpha("Daniel")
print(a.isAlive())
a.start()
a.join()
b.start()
b.join()
print(a.isAlive())
c.start()
c.join()
d.start()

