from bs4 import BeautifulSoup
import requests

def parse_ukd_data():
    url = "https://ukd.edu.ua"
    page = requests.get(url)
    array_professions = []
    soup = BeautifulSoup(page.content, "html.parser")
    professions = soup.find(class_='col-lg-9 col-md-12')
    tag_ul = professions.find('ul')
    name_professions = tag_ul.find_all('li')
    for values in name_professions:
        prof_name = values.text.strip()
        array_professions.append(prof_name)
    print("UKD professions parse list: ")
    print()

    writing = open('parse_ukd.txt', 'w')
    for elem in array_professions:
        print(elem)
        writing.write(elem + '\n ')
    writing.close()

parse_ukd_data()