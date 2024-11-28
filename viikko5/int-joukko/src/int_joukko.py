KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.maarita_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self.maarita_kasvatuskoko(kasvatuskoko)

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def maarita_kapasiteetti(self, kapasiteetti):
        if kapasiteetti == None:
            return KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        else:
            return kapasiteetti

    def maarita_kasvatuskoko(self, kasvatuskoko):
        if kasvatuskoko == None:
            return OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")
        else:
            return kasvatuskoko

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.kasvata_listaa()

    def kasvata_listaa(self):
        vanha_lista = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.ljono)

    def poista(self, luku):
        if not self.kuuluu(luku):
            return

        indeksi = self.ljono.index(luku)
        self.ljono.pop(indeksi)
        self.alkioiden_lkm -= 1

    def kopioi_lista(self, alkuperainen_lista, uusi_lista):
        alkuperaisen_listan_pituus = len(alkuperainen_lista)
        uusi_lista[alkuperaisen_listan_pituus:] = alkuperainen_lista

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        yhdiste = IntJoukko()

        for luku in joukko1.to_int_list() + joukko2.to_int_list():
            yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(joukko1, joukko2):
        leikkaus = IntJoukko()

        for luku in joukko1.to_int_list():
            if joukko2.kuuluu(luku):
                leikkaus.lisaa(luku)

        return leikkaus

    @staticmethod
    def erotus(joukko1, joukko2):
        erotus = IntJoukko()

        for luku in joukko1.to_int_list():
            if not joukko2.kuuluu(luku):
                erotus.lisaa(luku)

        return erotus

    def __str__(self):
        uusi_lista = self.ljono[:self.alkioiden_lkm]

        return "{" + ", ".join(map(str, uusi_lista)) + "}"
