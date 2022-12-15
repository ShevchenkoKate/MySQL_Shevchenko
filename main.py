import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, pymysql

API_TOKEN = '5719166402:AAH1hsxG6OJ53yR-spUx2ldXQ9_qfMKkeZE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет......\n Это наш первый тестовый бот")
    statistics(message.chat.id, message.text)
    stat(message.chat.id, message.text)

def statistics(user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%Y $H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])

def stat(user_id, command):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='bot',
                                 password='bot_KP11',
                                 database='bot')
    cursor = connection.cursor()
    data2 = datetime.datetime.today().strftime("%d-%m-%Y $H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data2))
    connection.commit()
    cursor.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
