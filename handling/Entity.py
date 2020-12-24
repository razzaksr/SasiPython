from sqlite3.dbapi2 import Date


class Jobcard:
    def __init__(self, cn=0, pd=Date(9999,9,9), cun="", cc=0, i=[], ed=0, eb=0, vn=""):
        self.jobNumber = cn
        self.pickedDate = pd
        self.custName = cun
        self.custContact = cc
        self.issues = i
        self.expectedDelivery = ed
        self.expectedBill = eb
        self.vehicleNumber=vn

    def __str__(self):
        return str(self.jobNumber) + " " +str(self.vehicleNumber)+" " + str(self.pickedDate) + " " + self.custName + " " + str(
            self.custContact) + " " + str(self.issues) + " " + str(self.expectedDelivery) + " " + str(
            self.expectedBill) + "\n"
