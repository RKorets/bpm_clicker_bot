import logging
import time
from aiogram import executor, types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
import tg_clicker

logging.basicConfig(level=logging.INFO)
bot = Bot('5275321950:AAFLbCRw5j6YK6hi76tD7A3wYvr6n3Jcdsc')

dp = Dispatcher(bot=bot)


def auth(func):
    async def wrapper(message):
        if message.chat.id != 368553201:
            return await message.answer(f'You dont have rules!')
        return await func(message)
    return wrapper


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    buttons = ['RUN', 'CONFIRM', 'You ID', 'Screen', 'OK Button']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer(f'Okey... chose some', reply_markup=keyboard)


@dp.message_handler(Text(equals=['RUN']))
@auth
async def run(message: types.message):
    tg_clicker.start()
    await bot.send_photo(message.chat.id, open('screen.png', 'rb'))


@dp.message_handler(Text(equals=['Screen']))
@auth
async def screen(message: types.message):
    tg_clicker.screen()
    await bot.send_photo(message.chat.id, open('screen.png', 'rb'))


@dp.message_handler(Text(equals=['OK Button']))
@auth
async def ok(message: types.message):
    tg_clicker.ok_button()
    await message.answer(f'Ok I click this button')


@dp.message_handler(Text(equals=['CONFIRM']))
@auth
async def confirm(message: types.message):
    await bot.send_message(message.chat.id, f'Ok wait 5 seconds')
    tg_clicker.confirm()
    await bot.send_photo(message.chat.id, open('screen.png', 'rb'))
    await bot.send_message(message.chat.id, f'If need continue press RUN button')


@dp.message_handler(Text(equals=['You ID']))
async def personal_id(message: types.message):
    await message.answer(f'{message.chat["first_name"]} you chat id - {message.chat.id}')


#bot.send_message(message.chat.id, f'Hi {message.text}')
#message.chat["first_name"]

if __name__ == "__main__":
    executor.start_polling(dp)