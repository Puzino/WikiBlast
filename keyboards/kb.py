from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb():
    kb_list = [[KeyboardButton(text="📖 Случайная статья")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def ease_link_kb(link: str):
    inline_kb_list = [
        [InlineKeyboardButton(text="Ссылка на статью", url=link)],
        # [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
        # [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)