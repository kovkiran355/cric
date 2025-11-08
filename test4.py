import requests
import json
from tabulate import tabulate

def fetch_cricket_score():
    url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/hscard"
    headers = {
        "x-rapidapi-key": "6efc557281mshce2d68c7f8aa843p1e5a21jsn0c509d80627c",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print(f"Status code: {response.status_code}")
    
    if response.status_code != 200:
        print("Failed to fetch data.")
        return
    
    data = response.json()
    scorecards = data.get("scorecard", [])

    if not scorecards:
        print("No scorecard data found.")
        return

    for idx, innings in enumerate(scorecards, 1):
        print(f"\n🏏 {'='*20} Innings {idx}: {innings.get('batteamname', 'Unknown')} {'='*20}\n")

        # Batting Table
        batsmen = innings.get("batsman", [])
        batting_table = []
        for b in batsmen:
            batting_table.append([
                b.get("name", ""),
                b.get("runs", 0),
                b.get("balls", 0),
                b.get("fours", 0),
                b.get("sixes", 0),
                b.get("strkrate", "0"),
                b.get("outdec", "")
            ])
        
        print("🧢 Batting Summary:")
        print(tabulate(batting_table, headers=["Name", "Runs", "Balls", "4s", "6s", "SR", "Dismissal"], tablefmt="grid"))

        # Extras and Total
        extras = innings.get("extras", {})
        total = innings.get("score", 0)
        wickets = innings.get("wickets", 0)
        overs = innings.get("overs", 0)
        runrate = innings.get("runrate", 0)

        print(f"\nExtras: {extras.get('total', 0)} | Total: {total}/{wickets} | Overs: {overs} | Run Rate: {runrate}\n")

        # Bowling Table
        bowlers = innings.get("bowler", [])
        bowling_table = []
        for bowler in bowlers:
            bowling_table.append([
                bowler.get("name", ""),
                bowler.get("overs", ""),
                bowler.get("runs", 0),
                bowler.get("wickets", 0),
                bowler.get("economy", ""),
                bowler.get("maidens", 0)
            ])
        
        print("🎯 Bowling Summary:")
        print(tabulate(bowling_table, headers=["Name", "Overs", "Runs", "Wkts", "Econ", "Maidens"], tablefmt="grid"))
        print("\n" + "="*70)

if __name__ == "__main__":
    fetch_cricket_score()
