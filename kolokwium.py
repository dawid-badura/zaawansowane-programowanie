class Pojazd:
    def __init__(self, marka, model, moc, rokProdukcji, kolor):
        self._marka = marka
        self._model = model
        self._moc = moc
        self._rokProdukcji = rokProdukcji
        self._kolor = kolor

    @property
    def marka(self) -> None:
        return self._marka

    @property
    def model(self) -> None:
        return self._model

    @property
    def moc(self) -> None:
        return self._moc

    @property
    def rokProdukcji(self) -> None:
        return self._rokProdukcji

    @property
    def kolor(self) -> None:
        return self._kolor

    def __str__(self):
        return f'Marka: {self._marka} Model: {self._model} Moc: {self._moc} Rok produkcji: {self._rokProdukcji} Kolor: {self._kolor}'


class Firma:
    def __init__(self, nazwa, rokPowstania, iloscPracownikow):
        self._nazwa = nazwa
        self._rokPowstania = rokPowstania
        self._iloscPracownikow = iloscPracownikow

    @property
    def nazwa(self) -> None:
        return self._nazwa

    @property
    def rokPowstania(self) -> None:
        return self._rokPowstania

    @property
    def iloscPracownikow(self) -> None:
        return self._iloscPracownikow


class FirmaTransportowa(Firma):
    def __init__(self, nazwa="Trans", rokPowstania=2014, iloscPracownikow=24):
        super(FirmaTransportowa, self).__init__(nazwa, rokPowstania, iloscPracownikow)

    @property
    def nazwa(self) -> None:
        return self._nazwa

    @property
    def rokPowstania(self) -> None:
        return self._rokPowstania

    @property
    def iloscPracownikow(self) -> None:
        return self._iloscPracownikow

    def __str__(self):
        return f'Nazwa firmy transportowej: {self._nazwa} Rok powstania: {self._rokPowstania} Ilość pracowników: {self._iloscPracownikow}'


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa="Food", rokPowstania=1997, iloscPracownikow=135):
        super(FirmaSpozywcza, self).__init__(nazwa, rokPowstania, iloscPracownikow)

    @property
    def nazwa(self) -> None:
        return self._nazwa

    @property
    def rokPowstania(self) -> None:
        return self._rokPowstania

    @property
    def iloscPracownikow(self) -> None:
        return self._iloscPracownikow

    def __str__(self):
        return f'Nazwa firmy spożywczej: {self._nazwa} Rok powstania: {self._rokPowstania} Ilość pracowników: {self._iloscPracownikow}'


class Odcinek:
    def __init__(self, AX, AY, BX, BY):
        self._AX = AX
        self._AY = AY
        self._BX = BX
        self._BY = BY

    @property
    def AX(self) -> None:
        return self._AX

    @property
    def AY(self) -> None:
        return self._AY

    @property
    def BX(self) -> None:
        return self._BX

    @property
    def BY(self) -> None:
        return self._BY


class Kurs:
    def __int__(self, pojazd, odcinek):
        self._pojazd = pojazd
        self._odcinek = odcinek

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @property
    def odcinek(self) -> Odcinek:
        return self._odcinek

    def nazwaPojazdu(self):
        return self.pojazd.marka

    def dlugoscOdcinka(self):
        return (((self.odcinek.BX - self.odcinek.AX) ** 2) + ((self.odcinek.BY - self.odcinek.AY) ** 2)) ** 0.5


P = Pojazd("Volvo", "X", 500, 2014, "niebieski")
O = Odcinek(1, 2, 1, 2)
K = Kurs(Pojazd, Odcinek)
print(K.nazwaPojazdu())
print(K.dlugoscOdcinka())
