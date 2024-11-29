from abc import ABC, abstractmethod

class Komento(ABC):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._tila_ennen_kumoamista = None

    @abstractmethod
    def suorita(self):
        pass

    def kumoa(self):
        if self._tila_ennen_kumoamista is not None:
            self._sovelluslogiikka.aseta_arvo(self._tila_ennen_kumoamista)

class Summa(Komento):
    def suorita(self):
        self._tila_ennen_kumoamista = self._sovelluslogiikka.arvo()
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.plus(arvo)

class Erotus(Komento):
    def suorita(self):
        self._tila_ennen_kumoamista = self._sovelluslogiikka.arvo()
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.miinus(arvo)
        
class Nollaus(Komento):
    def suorita(self):
        self._tila_ennen_kumoamista = self._sovelluslogiikka.arvo()

        self._sovelluslogiikka.nollaa()
        
class Kumoa(Komento):
    def suorita(self):
        pass