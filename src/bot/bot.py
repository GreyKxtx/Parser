from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.database.database import dbService

API_TOKEN = '5975408409:AAF9HEonla9oqlodSTjt1rjq5FkvT-TKlyk'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для отправки постов из базы данных в канал. Используйте /send_posts для отправки.")


@dp.message_handler(commands=['send_posts'])
async def send_posts(message: types.Message):
    all_posts = dbService.findMany({})

    # Отправка постов в личные сообщения
    for post in all_posts:
        post_message = f"<b>Источник:</b> {post[1]} \n<b>Заголовок:</b> {post[2]} \n<b>Дата:</b> {post[3]} \n<b>Текст:</b> {post[4]} \n<b>Ссылка:</b> {post[5]}"
        await message.answer(post_message, parse_mode=ParseMode.HTML)
        await types.ChatActions.typing(2)

    await message.answer("Посты были успешно отправлены вам в личные сообщения.")


@dp.message_handler(commands=['forward_posts'])
async def forward_posts(message: types.Message):
    all_posts = dbService.get_all_posts()
    channel_id = '@makeyourvibes'  # Замените на имя вашего канала или его ID

    # Пересылка постов в группу
    for post in all_posts:
        source, title, text, date, link = post
        post_message = f"<b>Источник:</b> {source}\n<b>Заголовок:</b> {title}\n<b>Текст:</b> {text}\n<b>Дата:</b> {date}\n<b>Ссылка:</b> {link}"
        await bot.send_message(chat_id=channel_id, text=post_message, parse_mode=ParseMode.HTML)
        await types.ChatActions.typing(2)

    await message.answer("Посты были успешно пересланы в канал.")

@dp.message_handler(commands=['get_posts'])
async def get_posts(message: types.Message):
    all_posts = dbService.get_all_posts()

    if all_posts:
        response = "Список постов:\n\n"
        for post in all_posts:
            source, title, text, date, link = post
            response += f"<b>Источник:</b> {source}\n<b>Заголовок:</b> {title}\n<b>Текст:</b> {text}\n<b>Дата:</b> {date}\n<b>Ссылка:</b> {link}\n\n"

        await message.answer(response, parse_mode=ParseMode.HTML)
    else:
        await message.answer("В базе данных нет записей.")

if __name__ == '__main__':
    from aiogram import executor

    if not dp.is_polling():
        executor.start_polling(dp, skip_updates=True)
