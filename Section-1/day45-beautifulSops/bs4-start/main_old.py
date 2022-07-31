from bs4 import BeautifulSoup
# import lxml

with open("C:\\MACE_SoftTech\\WebDevelopment\\day45-beautifulSops\\bs4-start\\website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)

# print(soup.title.name) # return the name of the tag
# print(soup.title.string) # return the string from the tag

# print("#" * 10)

# print(soup.prettify())

# print(soup.a)
# print(soup.ul.li.string)

# above code is holding the first elements from the file.
# how to hold all elements from the website.

all_anchor_tags = soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.getText())

