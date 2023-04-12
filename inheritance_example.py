class Animal:
    def __init__(self, name):
        self.myname = name

    def talk(self):
        raise NotImplementedError("subclass must implement abstract method")


class cat(Animal):
    def talk(self):
        return "Meow"


class dog(Animal):
    def talk(self):
        return "Barks"


class cow(Animal):
    def talk(self):
        return "Moos"


class horse(Animal):
    def talk(self):
        return "neighs"


class donkey(Animal):
    def talk(self):
        return "neighs"


paka = cat("whiskers")
doggy = dog("max")
bells = cow("milky")
farasi = horse("speed")
punda = donkey("runner")
print(paka.myname + ": " + paka.talk())
print(doggy.myname + " :" + doggy.talk())
print(bells.myname + " :" + bells.talk())
print(farasi.myname + " :" + farasi.talk())
print(punda.myname + " :" + punda.talk())
