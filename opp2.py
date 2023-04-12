class person:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def habari(self):
        print("Hello ,my name is "+self.myname+" and my age is "+str(self.myage))



class student(person):
    def __init__(self,name,age,studentid):
        super().__init__(name,age)
        self.mystudent=studentid

    def habari(self):
        super().habari()
        print("im a student with ID"+str(self.mystudent))

myname=student("DRILL",30,12345)
myname.habari()
