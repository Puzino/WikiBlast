from typing import Any

from utils.database import check_page_database, write_page_database
from wikipedia_func import get_wiki_page


def text_wiki_formatter(retry=5) -> tuple[str, Any] | None:
    """
    Return a random page summary and url from wikipedia API.
    :return: summary: str, url: str
    """
    if retry < 1:
        raise Exception("5 статей подряд уже находятся в базе.")

    title, summary, url, category = get_wiki_page()
    if not check_page_database(title):
        text = f"""<b>Название: {title}\nКатегория: {category}</b>\n\n{summary}"""
        write_page_database(title)
        return text, url
    else:
        return text_wiki_formatter(retry=(retry - 1))
