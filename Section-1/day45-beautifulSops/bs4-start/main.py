from encodings import utf_8


## import file
#
# with open("C:\\Users\\SushantJadhav\\Documents\\development\\Python-100-Days-Boot_Camp\\Section-1\\day45-beautifulSops\\bs4-start\\website.html", encoding="utf8") as file:
#     content = file.read()
#
#
#
# soup = bs4.BeautifulSoup(content, "html.parser")
#
# # print title
# # print(soup.title)
#
# # return name of the tag
# # print(soup.title.name)
#
# # return the string/value out of it.
# # print(soup.title.string)
#
# # # return the all links from URL.
# # for link in soup.find_all('a'):
# #     print(link.get('href'))
#
#
# # return all text from page
# # print(soup.get_text())
#
# find_all_atag = soup.find_all("p")
# # print(find_all_atag)
#
# heading = soup.select_one(".heading")
# print(heading)
#
# list = soup.find_all("li")
#
# print(list)

import bs4
import requests


response = requests.get("https://news.ycombinator.com/newest")

yc_web_page = response.text

soup = bs4.BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="a", class_="titlelink")
article_text = []
article_link = []
for article in article_tag:
    # print(article)
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]



# print(article_text)
# print(article_link)
# print(article_upvote)


largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(f"Score : {largest_number}")
print(article_text[largest_index])
print(article_link[largest_index])








