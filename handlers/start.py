from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from wikipedia_func import random_wiki_page
from keyboards.kb import main_kb, ease_link_kb
start_router = Router()



@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=main_kb())

@start_router.message(F.text == '📖 Случайная статья')
async def cmd_start_2(message: Message):
    title, summary, url, category = random_wiki_page()
    category = category.split(':')[1]
    text = f"""<b>Название: {title}\nКатегория: {category}</b>\n\n{summary}"""
    await message.answer(text, reply_markup=ease_link_kb(url))