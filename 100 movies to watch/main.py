import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

movie_data = response.text

soup = BeautifulSoup(movie_data,"html.parser")

movie_name = [data.get_text() for data in soup.find_all("h3","title")]

file = open('100 movie to watch!.txt','w')

for i in range(1,len(movie_name)+1):
    movie = movie_name[-i]
    file.write(f"{movie}\n")

file.close()
