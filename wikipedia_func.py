import random
import requests
import wikipediaapi
from fake_useragent import UserAgent


def random_wiki_page():
    ua = UserAgent().random # Random User-Agent
    cm_limit = "500"  # Pages limit
    RANDOM_CATEGORY = ['Информатика', 'Программирование', 'Компьютерные технологии', 'Компьютерная безопасность']
    CATEGORY = f'Категория:{random.choice(RANDOM_CATEGORY)}'
    URL = "https://ru.wikipedia.org/w/api.php"

    wiki_wiki = wikipediaapi.Wikipedia(user_agent=ua, language='ru')

    # Получаем список страниц из категории
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": CATEGORY,
    }

    response = requests.get(URL, params=params)
    data = response.json()

    if "query" in data:
        pages = data["query"]["categorymembers"]
        if pages:
            random_page = random.choice(pages)
            title = random_page['title']
            url = f'https://ru.wikipedia.org/wiki/{title.replace(" ", "_")}'
            page = wiki_wiki.page(title)
            return title, page.summary, url, CATEGORY
        else:
            print("Нет статей в данной категории.")
    else:
        print("Ошибка запроса.")
