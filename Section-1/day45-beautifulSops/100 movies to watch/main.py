import requests
from bs4 import BeautifulSoup
import re

movies_url_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# Write your code below this line 👇
url_text = movies_url_response.text

soup = BeautifulSoup(url_text, "html.parser")

movies_ranks = []
top_100_movies = []

movie_list = soup.find_all(name="h3", class_="title")

for item in movie_list:
    movies_list = item.getText()
    splited_movies_list = re.split(':|\)', movies_list)
    print(splited_movies_list)
    movie_ranking = int(splited_movies_list[0])
    movies_ranks.append(movie_ranking)
    top_movies = splited_movies_list[1]
    top_100_movies.append(top_movies.strip())

print(splited_movies_list)
# print(top_100_movies)

# print(movies)
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         print(movie)
#         file.write(f"{movie}\n")

# print(movies_title)
# for item in movie_list:
#     movies_list = item.getText()
#     splited_movies_list = re.split(':|\)', movies_list)
#     movie_ranking = int(splited_movies_list[0])
#     movies_ranks.append(movie_ranking)
#     top_movies = splited_movies_list[1]
#     top_100_movies.append(top_movies.strip())
#
# new_movies_order = []
#
# for rank in movies_ranks:
#     new_movies_order.insert(0, rank)
#
# for x in new_movies_order:
#     print(x + 1)
#     print(f"new movies : {movies_ranks[x]}")
#     # print(f"{x}) {top_100_movies[movies_ranks[x]]}")


