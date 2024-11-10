import requests
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.text import Text

def main():
    season = Prompt.ask("Select season [magenta][2023-24][/magenta]")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationalities = reader.get_nationalities()
    nationalities = f"[{'/'.join(nationalities)}]"
    nationality = Prompt.ask(f"Select nationality [magenta]{nationalities}[/magenta]")

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Top scorers of {nationality} season {season}")

    table.add_column("name")
    table.add_column("team")
    table.add_column("goals")
    table.add_column("assists")
    table.add_column("points")

    for player in players:
        table.add_row(
            Text(player.name, style='cyan'), Text(player.team, style='magenta'), Text(str(player.goals), style='green'),
            Text(str(player.assists), style='green'), Text(str(player.points), style='green')
            )

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
