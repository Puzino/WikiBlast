from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb():
    kb_list = [[KeyboardButton(text="📖 Случайная статья")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def ease_link_kb(link: str):
    inline_kb_list = [
        [InlineKeyboardButton(text="Ссылка на статью", url=link)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
