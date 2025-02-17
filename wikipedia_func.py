import random

import requests
import wikipediaapi
from fake_useragent import UserAgent


def random_wiki_page():
    ua = UserAgent().random  # Random User-Agent
    random_category = ['Информатика', 'Программирование', 'Компьютерные технологии', 'Компьютерная безопасность']
    category = f'Категория:{random.choice(random_category)}'
    url = "https://ru.wikipedia.org/w/api.php"

    wiki_wiki = wikipediaapi.Wikipedia(user_agent=ua, language='ru')

    # Получаем список страниц из категории
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "query" in data:
        pages = data["query"]["categorymembers"]
        if pages:
            random_page = random.choice(pages)
            title = random_page['title']
            url = f'https://ru.wikipedia.org/wiki/{title.replace(" ", "_")}'
            page = wiki_wiki.page(title)
            return title, page.summary, url, category
        else:
            raise Exception("Нет статей в данной категории.")
    else:
        raise Exception("Ошибка запроса.")
