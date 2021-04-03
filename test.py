import requests
from bs4 import BeautifulSoup
import inflection

def titles_generator(links):
    titles = []

    for link in links:
        print(link[href])

    return titles

site_code = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')

titles_generator(links)
