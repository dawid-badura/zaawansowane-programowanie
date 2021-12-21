from klasy.Budynek import Budynek


class Mieszkanie(Budynek):
    def __init__(self, rodzaj_budynku: str, powierzchnia: int, cena: int, rok_powstania: int, adres_mieszkania: str):
        super().__init__(rodzaj_budynku, powierzchnia, cena, rok_powstania)
        self._adres_mieszkania = adres_mieszkania

    @property
    def adres_mieszkania(self):
        return self._adres_mieszkania

    def __str__(self):
        return f"Rodzaj budynku: {self._rodzaj_budynku}" \
               f"Powierzchnia: {self._powierzchnia}" \
               f"Cena: {self._cena}" \
               f"Rok powstania: {self._rok_powstania}" \
               f"Adres mieszkania: {self._adres_mieszkania}"
