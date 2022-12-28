import requests
import telebot

bot = telebot.TeleBot("5945868302:AAE7qRA3a2sCciKoRVCCzPr0zXayXGYpJ-s")
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

@bot.message_handler(commands=["run"])
def send_welcome(message):
    bot.reply_to(message, "Бот для определения актуального курса валют.\nКоманда /USD для определения текущего курса доллара США. "
                          "\nКоманда /EUR - для Евро. \nКоманда /TRY для определния стоимости одной турецкой лиры.")

@bot.message_handler(commands=['USD'])
def send_welcome(message):
    var = res['Valute']['USD']['Value']
    bot.reply_to(message, f'Курс доллара США: {var}')

@bot.message_handler(commands=['EUR'])
def send_welcome(message):
    var = res['Valute']['EUR']['Value']
    bot.reply_to(message, f'Курс евро: {var}')

@bot.message_handler(commands=['TRY'])
def send_welcome(message):
    var = res['Valute']['TRY']['Value']
    bot.reply_to(message, f'Курс турецкой лиры: {var/10}')

bot.infinity_polling()