from klasy.Budynek import Budynek


class Dom(Budynek):
    def __init__(self, rodzaj_budynku: str, powierzchnia: int, cena: int, rok_powstania: int, adres_domu: str):
        super().__init__(rodzaj_budynku, powierzchnia, cena, rok_powstania)
        self._adres_domu = adres_domu

    @property
    def adres_domu(self):
        return self._adres_domu

    def __str__(self):
        return f"Rodzaj budynku: {self._rodzaj_budynku}" \
               f"Powierzchnia: {self._powierzchnia}" \
               f"Cena: {self._cena}" \
               f"Rok powstania: {self._rok_powstania}" \
               f"Adres domu: {self._adres_domu}"
