from abc import ABC, abstractmethod
from sovelluslogiikka import Sovelluslogiikka

class Komento(ABC):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    @abstractmethod
    def suorita(self):
        pass

class Summa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.plus(arvo)

class Erotus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.miinus(arvo)
        
        
class Nollaus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovelluslogiikka.nollaa()
        
        
class Kumoa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        pass