from bs4 import BeautifulSoup
import requests


def film_urls() -> list:
    # film_ids: list = list() FOR TESTING
    film_urls: list = list()
    page_counter = 2
    username = input('Enter your letterboxd username: ')

    url = 'https://letterboxd.com/' + username + '/films/diary'
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, 'lxml')
    a_tags = list(content.findChildren('a', {'class':'edit-review-button has-icon icon-16 icon-edit'}))

    for tag in a_tags:
        var = BeautifulSoup(str(tag), 'html.parser')
        film_id = var.find('a', {'class':'edit-review-button has-icon icon-16 icon-edit'})['data-film-id']
        film_url = content.find('td', {'class':'td-actions film-actions film-cell-' + str(film_id) + ' has-menu hide-when-logged-out'})['data-film-link']
        # film_ids.append(film_id) FOR TESTING
        film_urls.append(film_url)

    while(True):
        try:
            extra_url = 'https://letterboxd.com/' + username + '/films/diary/page/' + str(page_counter) + '/'
            extra_response = requests.get(extra_url, timeout=5)
            extra_content = BeautifulSoup(extra_response.content, 'lxml')
            scraper = list(extra_content.findChildren('a', {'class':'edit-review-button has-icon icon-16 icon-edit'}))
            
            if(len(scraper) != 0):
                for s in scraper:
                    val = BeautifulSoup(str(s), 'html.parser')
                    poster_id = val.find('a', {'class':'edit-review-button has-icon icon-16 icon-edit'})['data-film-id']
                    poster_url = extra_content.find('td', {'class':'td-actions film-actions film-cell-' + str(poster_id) + ' has-menu hide-when-logged-out'})['data-film-link']
                    # film_ids.append(poster_id) FOR TESTING
                    film_urls.append(poster_url)
                
                page_counter += 1
                # print(page_counter) FOR TESTING
            else:
                raise Exception('Page does not exist. Scrape complete.')

        except:
            break

    return film_urls