import re

str = "Hey), Copines is a good song; I like that song"

print(re.split('; |, |\*|\n ', str))