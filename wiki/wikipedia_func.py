import random

import mechanicalsoup
import wikipediaapi
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

CATEGORIES = ['Информатика',
              'Программирование',
              'Компьютерные технологии',
              'Компьютерная безопасность',
              'Компьютерная терминология',
              'Искусственный интеллект',
              'Алгоритмы и структуры данных',
              'Базы данных',
              'Робототехника',
              'Операционные системы',
              'Компьютерные сети',
              'Криптография'
              ]


def random_page():
    category = random.choice(CATEGORIES)
    url = 'https://ru.wikipedia.org/wiki/Служебная:RandomInCategory'
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    submit = browser.page.find('input', {'name': 'wpcategory'})
    submit['value'] = category
    button = browser.page.find('button', {'class': 'oo-ui-inputWidget-input oo-ui-buttonElement-button'})
    form = browser.select_form()
    form.choose_submit(button)
    browser.submit_selected()
    bs = BeautifulSoup(str(browser.page), 'lxml')
    title = bs.find('span', {'class': 'mw-page-title-main'}).text
    return title, category


def get_wiki_page():
    ua = UserAgent().random
    title, category = random_page()
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=ua, language='ru')
    if title:
        url = f'https://ru.wikipedia.org/wiki/{title.replace(" ", "_")}'
        page = wiki_wiki.page(title)
        return title, page.summary, url, category
    else:
        raise Exception("Не удалось получить статью.")
