class Magari:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")


class toyota(Magari):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.mynum_door = num_doors

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} car with {self.mynum_door} door started")


gari = toyota("premio", "saloon", 2023, 5)
gari.kuanzisha()


class Motorcycle:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")


class BMW(Motorcycle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        +
        self.myengine = engine_size

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} motorbike with {self.myengine} cc")


bike = BMW("yahama", "XL", 2019, 5000)
bike.kuanzisha()
