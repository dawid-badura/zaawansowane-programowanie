class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f'{self.area}, {self.rooms} {self.price} {self.address} {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f'{self.area}, {self.rooms} {self.price} {self.address} {self.floor}'

H1 = House("260m2", 12, 850000, "Tarnowskie Góry, Ogórkowa 21", "800m2")
F1 = Flat("70m2", 3, 400000, "Piekary Sląskie, Makowa 1", "70m2")
print(str(H1))
print(str(F1))