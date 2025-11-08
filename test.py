import requests
import json

url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/hscard"
headers = {
    "x-rapidapi-key": "6efc557281mshce2d68c7f8aa843p1e5a21jsn0c509d80627c",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
print("Response text:")
print(response.text)
