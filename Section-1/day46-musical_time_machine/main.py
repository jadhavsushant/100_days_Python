
# Day 46 - musical time machine

from bs4 import BeautifulSoup
import requests

year = input("What year would you like to trave to in YYY-MM-DD format: ")

songs_list_response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")
# print(url.text)
songs_response_text = songs_list_response.text


soup = BeautifulSoup(songs_response_text, "html.parser")
song_title = soup.select_one(selector=".'c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only'")
print(song_title)
# songs_title = soup.find_all(name="h3", id="title-of-a-story")
#
# for x in songs_title:
#     print(x.get("class"))

"c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"


# print(songs_title)


# for song in songs_title:
#     text = song.getText()
#     print("".join([s for s in text.strip().splitlines(True) if s.strip()]))
#     print()

#class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

# song_names = [song.getText() for song in songs_title]

# print(song_names)


# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.find_all("span", class_="pmc-paywall")
# song_names = [song.getText() for song in song_names_spans]
# print(song_names)