import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def test_tarkista_pelaaja(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
    
    def test_ei_pelaaja(self):
        player = self.stats.search("Ei pelaaja")
        if player == None:
            self.assertEqual(None, None)

    def test_tietyn_tiimin_pelaajat(self):
        tiimin_pelaajat = self.stats.team("PIT")
        self.assertEqual(len(tiimin_pelaajat),1)
        self.assertIn("Lemieux", [player.name for player in tiimin_pelaajat])

    def test_top_pelaajat_points(self):
        top_pelaajat = self.stats.top(2)
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
        self.assertEqual(top_pelaajat[1].name, "Lemieux")

    def test_top_pelaajat_goals(self):
        top_pelaajat = self.stats.top(2,SortBy.GOALS)
        self.assertEqual(top_pelaajat[0].name, "Lemieux")
        self.assertEqual(top_pelaajat[1].name, "Yzerman")

    def test_top_pelaajat_assists(self):
        top_pelaajat = self.stats.top(2,SortBy.ASSISTS)
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
        self.assertEqual(top_pelaajat[1].name, "Yzerman")   