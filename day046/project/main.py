from bs4 import BeautifulSoup
import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"

should_ask_date = True
while should_ask_date:
    target_year = input("What year do you want to travel to?\nInput in this format YYYY-MM-DD: ")
    try:
        date = datetime.date.fromisoformat(target_year)
        should_ask_date = False
    except ValueError:
        print("Invalid format. Try again please!")

url = f"{BILLBOARD_BASE_URL}/{target_year}"
response = requests.get(url)
response.raise_for_status()
contents = response.text

with open("website.html", "r") as html_file:
    contents = html_file.read()

bs = BeautifulSoup(contents, "html.parser")
chart_list_items = bs.find_all(name="ul", class_="o-chart-results-list-row")

track_uris = []
scope = "playlist-modify-private"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), client_credentials_manager=SpotifyClientCredentials())

i = 1
for row in chart_list_items:
    song_data = row.find_all("li")[3]
    track = song_data.find("h3").getText().strip()
    artist = song_data.find("span").getText().strip()
    query = f"artist:{artist} track:{track} year:{str(date.year)}"
    print(f"{i}) Searching for: {query}")
    track_result = spotify.search(q=query, type="track")
    tracks_founded = track_result["tracks"]["items"]
    i += 1
    if len(tracks_founded) > 0:
        track_uris.append(tracks_founded[0]["uri"])

if len(track_uris) > 0:
    print(f"Found {len(track_uris)}/100")
    user = spotify.current_user()
    playlist = spotify.user_playlist_create(user=user["id"], name=f"{str(date)} Billboard 100", public=False, description=f"Billboard 100 songs from {str(date.year)}")
    spotify.playlist_add_items(playlist["id"], items=track_uris)
    print("Playlist created!\n" + playlist["external_urls"]["spotify"])
else:
    print(f"Sorry! No tracks found in Spotify.")
