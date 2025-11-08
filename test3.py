import requests
import pandas as pd
import json

def fetch_cricket_scores():
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/hscard"
    headers = {
        "x-rapidapi-key": "6efc557281mshce2d68c7f8aa843p1e5a21jsn0c509d80627c",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Request failed ({response.status_code}):", response.text)
        return

    data = response.json()

    # Safely check what keys exist
    if "scoreCard" not in data:
        print("⚠️ 'scoreCard' key not found. Here's the JSON:")
        print(json.dumps(data, indent=2))
        return

    # Iterate through innings
    for innings in data["scoreCard"]:
        print(f"\n🏏 INNINGS: {innings.get('batTeamDetails', {}).get('batTeamName', 'Unknown')}")
        print("=" * 60)

        # 🏏 Batsmen Table
        batsmen = innings.get("batTeamDetails", {}).get("batsmenData", {})
        if batsmen:
            bat_rows = []
            for b in batsmen.values():
                bat_rows.append({
                    "Batsman": b.get("batName", ""),
                    "Runs": b.get("runs", ""),
                    "Balls": b.get("balls", ""),
                    "4s": b.get("fours", ""),
                    "6s": b.get("sixes", ""),
                    "SR": b.get("strikeRate", ""),
                    "Dismissal": b.get("outDesc", "")
                })
            print("\n Batsmen Summary:")

