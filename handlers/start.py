from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.kb import main_kb, ease_link_kb
from wiki.wikipedia_func import CATEGORIES, text_wiki_formatter

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    text = "Бот для отправки случайной статьи по темам: <b>%s</b>" % '\n'.join(CATEGORIES)
    await message.answer(text, reply_markup=main_kb())


@start_router.message(F.text == '📖 Случайная статья')
async def cmd_start_2(message: Message):
    await message.answer("Doing a request.. Wait please!")
    text, url = text_wiki_formatter()
    await message.answer(text, reply_markup=ease_link_kb(url))
