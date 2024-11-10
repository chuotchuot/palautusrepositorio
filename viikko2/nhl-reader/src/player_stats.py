from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        players_of_wanted_nationality = []
        for player in players:
            if player.nationality == nationality:
                players_of_wanted_nationality.append(player)

        players_of_wanted_nationality.sort(key=lambda player:player.points, reverse=True)

        return players_of_wanted_nationality