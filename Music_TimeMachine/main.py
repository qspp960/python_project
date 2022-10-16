import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

SPOTIFY_APP_CLIENT_ID = 'ba2d53a7e40b4f08a3b0d8782d545275'
SPOTIFY_APP_CLIENT_SECRET = '4803431fa49842afb0222e979db2825d'
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
REDIRECT_URI = "https://www.example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_APP_CLIENT_ID,
        client_secret=SPOTIFY_APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

user_input = input("Which year do you want to travel to? Type the data this format YYYY-MM-DD:")
response = requests.get(url=f"{BILLBOARD_URL}/{user_input}/")
billboard_data = response.text

soup = BeautifulSoup(billboard_data,"html.parser")
musics = soup.select("li ul li h3")
musicians = soup.select("li ul li span")

music_list = [music.getText().strip() for music in musics]
musician_list = []

for musician in musicians:
    check = musician.getText().strip()
    if 65 <= ord(check[0]) <= 122:
        musician_list.append(check)

year = user_input.split('-')[0]
song_uri = []
for music in music_list:
    result = sp.search(q=f'track:{music} year:{year}',type='track')

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user=user_id,name=f"{year} Billboard Chart 100!",public=False)
sp.playlist_add_items(playlist_id=playlist_id['id'],items=song_uri)
#pp = pprint.PrettyPrinter()
#pp.pprint(song_uri)