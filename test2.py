import requests
import json

url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/hscard"
headers = {
    "x-rapidapi-key": "6efc557281mshce2d68c7f8aa843p1e5a21jsn0c509d80627c",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if 'typeMatches' in data:
        matches = data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']
        print(matches)
    else:
        print("Key 'typeMatches' not found. Full response:")
        print(json.dumps(data, indent=2))
else:
    print("Request failed:", response.status_code, response.text)
