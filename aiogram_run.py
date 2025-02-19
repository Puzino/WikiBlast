import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from decouple import config

from create_bot import bot, dp
from handlers.start import start_router
from keyboards.kb import ease_link_kb
from wiki.wikipedia_func import text_wiki_formatter

CHAT_ID = config("CHAT_ID")

scheduler = AsyncIOScheduler()


async def send_scheduled_message() -> None:
    """
    Async func for send wiki page from scheduler
    :return: None
    """
    try:
        text, url = text_wiki_formatter()  # Get info
        await bot.send_message(CHAT_ID, text, reply_markup=ease_link_kb(url))  # Sending message to chat id
        logging.info("Message sent successfully!")
    except Exception as e:
        text = f"Message sending error: {e}"
        logging.error(text)
        await bot.send_message(CHAT_ID, text)


async def main() -> None:
    """
    Main func aiogram bot
    :return: None
    """
    dp.include_router(start_router)
    # Schedule setting: dispatch at 9:00, 13:00 and 18:00
    scheduler.add_job(send_scheduled_message, "cron", hour=9, minute=0)
    scheduler.add_job(send_scheduled_message, "cron", hour=13, minute=0)
    scheduler.add_job(send_scheduled_message, "cron", hour=18, minute=0)

    scheduler.start()  # Starting the scheduler
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
