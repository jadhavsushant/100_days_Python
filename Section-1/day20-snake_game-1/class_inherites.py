class Dad:
    def __init__(self):
        self.name = "Daulat Patil"
        self.car = "Maruti-800"

    def home(self):
        print("Single Story Building")

    def farm(self):
        print("5 Acer of farm")


class Son(Dad):
    def __init__(self):
        super().__init__()
        self.name = "Yashvant"

    def home(self):
        super().home()
        print("Double story building")

    def farm(self):
        super().farm()


dad = Dad()
son = Son()


print(dad.name)
print(son.name)
son.home()
print(son.car)
son.farm()