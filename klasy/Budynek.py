class Budynek:
    def __init__(self, rodzaj_budynku: str, powierzchnia: int, cena: int, rok_powstania: int):
        self._rodzaj_budynku = rodzaj_budynku
        self._powierzchnia = powierzchnia
        self._cena = cena
        self._rok_powstania = rok_powstania

    @property
    def rodzaj_budynku(self):
        return self._rodzaj_budynku

    @property
    def powierzchnia(self):
        return self._powierzchnia

    @property
    def cena(self):
        return self._cena

    @property
    def rok_powstania(self):
        return self._rok_powstania

    def __str__(self):
        return f"Rodzaj budynku: {self._rodzaj_budynku}" \
               f"Powierzchnia: {self._powierzchnia}" \
               f"Cena: {self._cena}" \
               f"Rok powstania: {self._rok_powstania}"
