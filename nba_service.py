from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd


def find_player_id(name):
    all_players = players.get_players()

    for p in all_players:
        if p["full_name"].lower() == name.lower():
            return p["id"]

    return None
# Function to get players stats
def get_player_stats (name, season):

    # Check if player id is valid
    player_id = find_player_id(name)

    if not player_id:
        return {"error": "Player not found"}
    
    gamelog = playergamelog.PlayerGameLog(
        player_id=player_id,
        season=season
    )
    # Use pandas to grab raw data table from nba
    df = gamelog.get_data_frames()[0]

    return {
        "player": name,
        "ppg": round(float(df["PTS"].mean()), 1),
        "ast": round(float(df["AST"].mean()), 1),
        "reb": round(float(df["REB"].mean()), 1)
    }

def compare_players(name1, name2, season):
    stats1 = get_player_stats(name1, season)
    stats2 = get_player_stats(name2, season)
    
    if "error" in stats1 or "error" in stats2:
        return {"error": "One or more players not found"}
    
    return {"player1": stats1, "player2": stats2}


