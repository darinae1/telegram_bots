from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils import executor
import logging
import os
import datetime


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, я бот, который отправит'
                                                 f' тебе твоё же сообщение', reply_markup=user_kb)
    await bot.send_message(message.from_user.id, 'Можешь узнать дату', reply_markup=user_inline_kb)


@dp.message_handler(text='Доброе утро⛅')
async def good_morning(message: types.Message):
    await bot.send_message(message.from_user.id, f'Доброе утро, {message.from_user.first_name}!')


@dp.message_handler(text='Доброй ночи🌙')
async def good_night(message: types.Message):
    await bot.send_message(message.from_user.id, f'Спокойной ночи, {message.from_user.first_name}!')


@dp.callback_query_handler(text='button_date')
async def date_message(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, 'Кнопка сработала', show_alert=True)

    now_date = datetime.datetime.now()

    await bot.send_message(callback_query.from_user.id, f'{now_date.strftime("%d.%m.%Y %H:%M:%S")}')


@dp.message_handler()
async def reply_message(message: types.Message):
    await message.reply(message.text)


"""*************************************  BUTTONS  ******************************************"""
button_good_morning = KeyboardButton('Доброе утро⛅')
button_good_night = KeyboardButton('Доброй ночи🌙')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_good_morning)\
    .add(button_good_night)


button_date = InlineKeyboardButton(text='Время и дата', callback_data='button_date')
user_inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(button_date)


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)