from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
import aiofiles
from little_big_bot.config import number, count_of_attempts

bot = Bot('5417083958:AAH1WwqO1oG6x52fKN3W6R7_mOAmFp4Nb9A')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    if count_of_attempts == 1:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name},'
                                                     f' я загадал число, попробуй его угадать')
    else:
        await bot.send_message(message.from_user.id, 'Введите число')


@dp.message_handler()
async def info(message: types.Message):
    try:
        global count_of_attempts
        if int(message.text) == number:
            await message.answer(f'Поздравляю! Вы угадали!\nКоличество попыток: {count_of_attempts}')
            count_of_attempts = 1
        elif int(message.text) < number:
            await message.answer('Ваше число меньше загаданного\nПопробуй ввести число еще раз')
            count_of_attempts += 1
        else:
            await message.answer('Ваше число больше загаданного\nПопробуй ввести число еще раз')
            count_of_attempts += 1
    except:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name},'
                                                     f' я загадал число, попробуй его угадать')


if __name__ == '__main__':
    print('Бот запущен')
    executor.start_polling(dp, skip_updates=True)
