# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
# logiczną, pozytywną gdy ocena jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
# obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if(self.marks >50):
            return True
        else:
            return False

Andrzej = Student("Andrzej", 58)
Adam = Student("Adam", 49)

print(Andrzej.is_passed())
print(Adam.is_passed())