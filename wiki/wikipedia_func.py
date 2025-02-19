import random

import mechanicalsoup
import wikipediaapi
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from database.database import check_page_database, write_page_database

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


def random_page() -> tuple:
    """
    Get random page from wikipedia and clean title.
    :return: title: str, category: str
    """
    category = random.choice(CATEGORIES)  # Choice random category from list
    url = 'https://ru.wikipedia.org/wiki/Служебная:RandomInCategory'
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    submit = browser.page.find('input', {'name': 'wpcategory'})  # Find input area
    submit['value'] = category  # Write a category to input
    button = browser.page.find('button', {'class': 'oo-ui-inputWidget-input oo-ui-buttonElement-button'})  # Find button
    form = browser.select_form()  # Create form
    form.choose_submit(button)  # Add button to form
    browser.submit_selected()  # Sending a changes
    bs = BeautifulSoup(str(browser.page), 'lxml')
    title = bs.find('span', {'class': 'mw-page-title-main'}).text  # Find main tag title
    return title, category


def get_wiki_page() -> tuple | None:
    """
    Get clean page from wikipedia with title, summary, url, category.
    :return: title: str, summary: str, url: str, category: str
    """
    ua = UserAgent().random  # Create random user-agent
    title, category = random_page()  # Get clean title
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=ua, language='ru')
    if title:
        url = f'https://ru.wikipedia.org/wiki/{title.replace(" ", "_")}'  # Create url
        page = wiki_wiki.page(title)  # Get clean page by title
        return title, page.summary, url, category
    else:
        raise Exception("Failed to retrieve the article.")  # Raise an error


def text_wiki_formatter(retry: int = 5) -> tuple | None:
    """
    The main function returns the formatted text.
    Recursive function, checks the database for a duplicate, if a duplicate is present, recurses to get new information.
    Return a random page summary and url from :func: get_wiki_page.
    :return: summary: str, url: str
    """
    if retry < 1:  # Check recursive for stop
        raise Exception("5 articles in a row are already in the database.")

    title, summary, url, category = get_wiki_page()  # Get information
    if not check_page_database(title):  # Check database
        text = f"""<b>Название: {title}\nКатегория: {category}</b>\n\n{summary}"""
        write_page_database(title)  # Write information in database
        return text, url
    else:
        return text_wiki_formatter(retry=(retry - 1))  # If database exists info return recursive
