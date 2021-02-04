import requests
from bs4 import BeautifulSoup
import re


def make_request(keyword):
    r = requests.get(f'https://maoridictionary.co.nz/search?keywords={keyword}')
    return r.text


def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()


def get_definitions(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')

    results = soup.find_all("section", class_="")

    phrases = []
    for result in results:
        print(result)
        print()
        phrase = clean_text(result.find(class_="title").find(text=True))

        if phrase == "Found 0 matches":
            return None

        definitions = []
        for definition in result.find_all(class_="detail"):
            meaning = clean_text(definition.find("p", class_="").get_text())
            source = clean_text(definition.find("p", class_="example").get_text())

            definition_dict = {
                'meaning': meaning,
                'source': source if source != "" else None
            }

            definitions.append(definition_dict)

        phrase_dict = {
            'phrase': phrase,
            'definitions': definitions
        }

        phrases.append(phrase_dict)

    return phrases
