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

max_value: int = 0
max_director: list = list()

for key in directors:
    if(directors[key] >= max_value):
        max_value = directors[key]
        max_director.append(key)

if(len(max_director) == 1):
    print(f"\nYour most watched director is {max_director}!\n")
    print(f"You have seen {directors[max_director]} films directed by {max_director}, which is {((max_value/total_films) * 100):.2f}% of the films you have logged.\n")
else:
    print("\nYour most watched directors are: ")
    for d in max_director:
        print(d + ', ', end='')
    print(" and... that's it!\n", end='')
    print(f"\nYou have seen {max_value} films from each of these directors, which is {((max_value*len(max_director)/total_films)*100):.2f}% of the films you have logged.\n")

# Sean Fenessey
# Your most watched directors are: 
# Robert Aldrich, Jane Campion, Francis Ford Coppola, Wes Craven, Steven Soderbergh, Martin Scorsese,  and... that's it!
# You have seen 17 films from each of these directors, which is 5.71% of the films you have logged.