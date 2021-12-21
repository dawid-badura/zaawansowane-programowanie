from klasy.Zamówienie import Zamówienie
from klasy.Developer import Developer
from klasy.Mieszkanie import Mieszkanie
from klasy.Dom import Dom

Developer1 = Developer("Andrzej", "Kowalski", "Kowalski S.A.", 2003)
M1 = Mieszkanie("Mieszkanie numer 1", 45000, 205000, 2018, "Ogrodowa 12")
M2 = Mieszkanie("Mieszkanie numer 2", 63000, 320000, 2020, "Kasztanowa 1")
D1 = Dom("Dom numer 1", 140000, 721000, 2021, "Łąkowa 19")
Z = Zamówienie(1, "Jacek Laskowski", Developer1, [
    M1,
    M2,
    D1
])
print(str(Z))
print("Wartość zamówienia:", Z.wartosc_zamowienia())
print("Łączna liczba metrów kwadratowych:", Z.metry_kwadratowe())
