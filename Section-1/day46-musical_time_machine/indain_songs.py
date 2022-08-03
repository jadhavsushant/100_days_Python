from bs4 import BeautifulSoup
import requests

url = "https://www.jiosaavn.com/s/playlist/phulki_user/Monthly_Top_100_-_Hindi/PZaVnbecD1rfemJ68FuXsA__"

response = requests.get(url)
response_text = response.text


soup = BeautifulSoup(response_text, "html.parser")
# song_list = soup.find(name="text")
songs_list = soup.select(selector="h4 a")

top100_songs = []
for x in songs_list:
    top100_songs.append(x.getText("text"))

print(top100_songs)