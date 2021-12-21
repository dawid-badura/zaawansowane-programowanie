class Zamówienie():
    def __init__(self, id_zamowienia: int, dane_zamawiajacego: str, dane_developera: str, nieruchomosci: list):
        self._id_zamowienia = id_zamowienia
        self._dane_zamawiajacego = dane_zamawiajacego
        self._nieruchomosci = nieruchomosci
        self._dane_developera = dane_developera

    @property
    def id_zamowienia(self):
        return self._id_zamowienia

    @property
    def dane_zamawiajacego(self):
        return self._dane_zamawiajacego

    @property
    def dane_developera(self):
        return self._dane_developera

    @property
    def nieruchomosci(self):
        return self._nieruchomosci

    @nieruchomosci.setter
    def nieruchomosci(self, nieruchomosci: list):
        self._nieruchomosci = nieruchomosci

    def __str__(self):
        return f"Id zamówienia: {self._id_zamowienia}" \
               f"Dane developera: {self._dane_developera}" \
               f"Dane zamawiającego: {self._dane_zamawiajacego}" \
               f"Nieruchomości: {''.join(str(nieruchomosc) for nieruchomosc in self._nieruchomosci)}"

    def wartosc_zamowienia(self):
        laczna_wartosc = 0
        for nieruchomosc in self._nieruchomosci:
            laczna_wartosc += nieruchomosc.cena
        return laczna_wartosc

    def metry_kwadratowe(self):
        laczna_wartosc_metrow_kwadratowych = 0
        for nieruchomosc in self._nieruchomosci:
            laczna_wartosc_metrow_kwadratowych += nieruchomosc.powierzchnia
        return laczna_wartosc_metrow_kwadratowych
