# MutyalaHarshith Creations

import telebot
import requests
from telebot.types import InlineKeyboardButton

# Fillout Here The BotToken it gets from botfather further queries @MutyalaHarshith 0n telegram
bot = telebot.TeleBot('CAACAgUAAxkBAAIYeGK1ZXx-OIpekd6pG4JWFIT5ZPtzAAIhBgAC3ZD5V8DbuSeu9KvqHgQ')

while True:
    try:

        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton(text='Generate email'))
        keyboard.add(InlineKeyboardButton(text='Refresh inbox'))
        keyboard.add(InlineKeyboardButton(text='About'))


        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id,
'''
π»ππ¦ π,
πππππππ π‘π ππ» ππππ ππππ π΅ππ‘ π

ππ πππ
βͺπ₯ ππ πΊππππππ‘π ππππππ  ππ¦ ππππππππ ππ π‘βπ ππ’π‘π‘ππ "πΊππππππ‘π πππππ"
βͺπ₯ ππ ππππππ β π¦ππ’π πππππ₯ πππππ ππ π‘βπ ππ’π‘π‘ππ "ππππππ β πππππ₯"
βͺπ₯ π΄ππ‘ππ π πππ€ πππ‘π‘ππ πππππ£ππ , π¦ππ’ π€πππ π ππ π ππ’π‘π‘ππ π€ππ‘β π π π’πππππ‘ ππππ, πππππ ππ π‘βππ  ππ’π‘π‘ππ π‘π ππππ π‘βπ πππ π πππ.
                              
π·ππ£ππππ£ππππ : @MutyalaHarshith
''',
                             reply_markup=keyboard)


        @bot.message_handler(content_types=['text'])
        def send_text(message):
            if message.text.lower() == 'generate email':
                email = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
                ekeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                ekeyboard.add(InlineKeyboardButton(text='Generate email'))
                ekeyboard.add(InlineKeyboardButton(text='Refresh inbox\n[' + str(email) + "]"))
                ekeyboard.add(InlineKeyboardButton(text='About'))
                bot.send_message(message.chat.id, "Your Temporary E-mail:")
                bot.send_message(message.chat.id, str(email), reply_markup=ekeyboard)
            elif message.text.lower() == 'refresh inbox':
                bot.send_message(message.chat.id, 'First, generate an email', reply_markup=keyboard)
            elif message.text.lower() == 'about':
                bot.send_message(message.chat.id,
'''
πβππ‘ ππ  ππ» ππππ ππππ π ?
- ππ‘ ππ  π πππππ₯ πππππ π πππ£πππ π‘βππ‘ πππππ€π  π‘π ππππππ£π πππππ ππ‘ π π‘ππππππππ¦ ππππππ π  π‘βππ‘ π πππ-πππ π‘ππ’ππ‘ππ πππ‘ππ π ππππ‘πππ π‘πππ πππππ ππ . πΌπ‘ ππ  πππ π ππππ€π ππ¦ πππππ  ππππ π‘πππππππ, 10ππππ’π‘πππππ, 10πππππππ, π‘βπππ€ππ€ππ¦ πππππ, ππππ-ππππ , ππππ πππππ πππππππ‘ππ, ππ’ππππ ππππ ππ π‘πππ β-ππππ
ππ»ππ€ πΈπππ ππππ ππππ π΅πππππ πππππ πππ’?β‘
- ππ πππ π‘βπ π‘ππππππππ¦ ππππ πππππ€π  π¦ππ’ π‘π πππππππ‘πππ¦ ππππ‘πππ‘ π¦ππ’π ππππ πππππππ₯ ππππππ π‘ π‘βπ πππ π  ππ ππππ ππππ ππππππππ‘πππ. πππ’π π‘ππππππππ¦ π-ππππ ππππππ π  ππ  πππππππ‘πππ¦ πππππ¦πππ’π . πππ’π πππ‘ππππ : ππππππππ‘πππ ππππ’π‘ π¦ππ’π ππππ ππ πππ π’π πππ  π€ππ‘β π€βππ π¦ππ’ πππππ’πππππ‘π, πΌπ-ππππππ π , π-ππππ ππππππ π  πππ ππππ‘πππ‘ππ πππ πππππππ‘πππ¦ πππππππππ‘πππ.

βͺ π΅ππ‘ ππππ : ππ» ππππ ππππ
βͺ πΆππππ‘ππ : @MutyalaHarshith
βͺ πΏππππ’πππ : ππ¦π‘βππ
βͺ ππ»πΏππππ’πππ : πΈπ | ππΈ
βͺ π»ππ π‘ππ : π»πππππ’ & πππ‘ππ‘π''')
            elif message.text.lower()[14] == "[":
                email = message.text.lower()[15:message.text.lower().find("]")]
                bkeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                bkeyboard.add(InlineKeyboardButton(text='Refresh inbox\n[' + str(email) + "]"))
                bkeyboard.add(InlineKeyboardButton(text='Generate email'))
                try:
                    data = requests.get(
                        "https://www.1secmail.com/api/v1/?action=getMessages&login=" + email[:email.find(
                            "@")] + "&domain=" + email[email.find("@") + 1:]).json()
                    if 'id' in data[0]:
                        for i in range(len(data)):
                            id = data[i]['id']
                            subject = data[i]['subject']
                            fromm = data[i]['from']
                            date = data[i]['date']
                            if len(subject) > 15:
                                subject = str(subject[0:15]) + "..."
                            bkeyboard.add(InlineKeyboardButton(
                                text=str(subject) + "\n from: " + fromm + " in " + "[id" + str(id) + "][" + str(
                                    email) + "]"))
                            bot.send_message(message.chat.id,
                                             "Subject: " + subject + "\n From: " + fromm + "\n Date:" + date,
                                             reply_markup=bkeyboard)
                            count = i + 1
                        bot.send_message(message.chat.id, "Here " + str(
                            count) + " message we're found\nClick on the below button to read the message\n\n Further Queries @MHGcHaT")
                    else:
                        bot.send_message(message.chat.id, 'Nothing found', reply_markup=bkeyboard)
                except BaseException:
                    bot.send_message(message.chat.id, 'No messages were received...', reply_markup=bkeyboard)
            elif message.text.lower().find("[id"):
                try:
                    data = message.text.lower()[message.text.lower().find("[id"):]
                    id = data[data.find("[") + 3:data.find(']')]
                    email = data[data.find("][") + 2:-1]
                    msg = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=" + email[:email.find(
                        "@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + id).json()
                    bot.send_message(message.chat.id,
                                     'Message βοΈ\n\n   From: ' + msg['from'] + "\n   Subject: " + msg[
                                         'subject'] + "\n   Date: " + msg[
                                         'date'] + "\n   text: " + msg['textBody'])
                except BaseException:
                    pass


        bot.polling(none_stop=True, interval=1, timeout=5000)
    except BaseException:
        pass
        
#MutyalaHarshith Develoveper Created By ΰ°ΰ±ΰ°€ΰ±ΰ°°ΰ°Ώΰ°? ΰ°?ΰ±ΰ°§ΰ°Έΰ±ΰ°Έΰ± 2022 
