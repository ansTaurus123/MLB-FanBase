import requests

MLB_API_BASE = "https://statsapi.mlb.com/api/v1"

def fetch_player_stats(player_id):
    response = requests.get(f"{MLB_API_BASE}/people/{player_id}/stats")
    return response.json()

