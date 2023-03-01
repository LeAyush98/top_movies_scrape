from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

html = response.text

tomato = BeautifulSoup(html, "html.parser")

movie_list =   tomato.select(selector="div.gallery div.article-title-description div.article-title-description__text h3.title")

count = 100

movie_staged = []

for _ in movie_list:
    try:
        movie_staged.append(f"{count}) {_.getText().split(') ')[1]}")
    except IndexError:
        movie_staged.append(f"{count}) {_.getText().split(': ')[1]}")
    finally:        
        count -=1

file = open("movies.txt", "w", encoding="utf-8")

count +=1

for movie in movie_staged:
    file.write(f"{movie_staged[-count]} \n\n")
    count +=1 
