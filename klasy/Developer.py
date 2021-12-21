class Developer:
    def __init__(self, imie: str, nazwisko: str, nazwa_firmy: str, rok_powstania: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nazwa_firmy = nazwa_firmy
        self._rok_powstania = rok_powstania

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy

    @property
    def rok_powstania(self):
        return self._rok_powstania

    def __str__(self):
        return f"Imię i nazwisko: {self._imie} {self._nazwisko} " \
               f"Nazwa firmy i rok powstania: {self._nazwa_firmy} {self._rok_powstania}"
