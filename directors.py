from bs4 import BeautifulSoup
import requests
from webscraper import film_urls

films = film_urls()
directors = {}
total_films: int = len(films)

for f in films:
    try:
        url = 'https://letterboxd.com' + f + 'crew/'
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, 'lxml')
        director = content.find('span', {'class':'prettify'}).text
        if(director in directors):
            directors[director] += 1
        else:
            directors[director] = 1
    
    except:
        print(f"no director at {url}")

max_director: list = list()
num_films_directed = directors.values()
max_value = max(num_films_directed)

for key in directors:
    if(directors[key] == max_value):
        max_director.append(key)

if(len(max_director) == 1):
    print(f"\nYour most watched director is {max_director[0]}!\n")
    print(f"You have seen {directors[max_director[0]]} films directed by {max_director[0]}, which is {((max_value/total_films) * 100):.2f}% of the films you have logged.\n")
else:
    print("\nYour most watched directors are: ")
    for d in max_director:
        print(d + ', ', end='')
    print("and... that's it!\n", end='')
    print(f"\nYou have seen {max_value} films from each of these directors, which makes up {((max_value*len(max_director)/total_films)*100):.2f}% of the films you have logged.\n")

# User Martin_Blanke
# Your most watched director is Alfred Hitchcock!

# You have seen 19 films directed by Alfred Hitchcock, which is 3.80% of the films you have logged.
