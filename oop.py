class Fruits:
    def __init__(self, type, colour, price):
        self.mytype = type
        self.mycolour = colour
        self.myprice = price

    def onyesha(self):
        print(self.mytype, self.mycolour, self.myprice)


# create an object
myobj=Fruits("Banana","Yellow",20)
myobj.onyesha()

class Employess:
    def __init__(self,name,salary):
        self.myname=name
        self.mysalary=salary

    def show(self):
        print(self.myname,self.mysalary)

myemp=Employess("DRILL",5000)
myemp.show()