# class: bundle objects and functions works over those objects

class Kart:
    __account=""
    __address=""
    __items=[]
    def setAccount(self,name):self.__account=name
    def setAddress(self,loc):self.__address=loc
    def setItems(self,it):self.__items=it
    def getAccount(self):return self.__account
    def getAddress(self):return self.__address
    def getItems(self):return self.__items
    def detail(self):print(self.__account,self.__address,self.__items)


k1=Kart()
k1.setAccount("Sasikumar")
k1.setAddress("Tiruchengode")
k1.setItems(["Bata","HP","Walmart"])
#k1.__account="sasikumar"
#k1.__address="Tiruchengode"
#k1.__items.append("Bata");k1.__items.append("HP Pendrive");k1.__items.append("Rebok")
#print(k1.account,k1.address,k1.items)
k1.detail()


k2=Kart()
k2.setAccount("Mohamed")
k2.setAddress("Salem")
k2.setItems(["Wall paper","Vaio","Dell"])
print(k2.getItems(),k2.getAddress())
