import telebot
import os
from telebot import types

bot = telebot.TeleBot("918949126:AAEWTT_DyGi1QXHwzJYREMAkc7LctHk1Ip4") 
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Расписание 📋')
keyboard1.row('Тех. поддержка 📩')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Уроки 📆')
keyboard2.row("Звонки ⏰")
keyboard2.row("Назад")
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row("Понедельник 1⃣", "Четверг 4⃣")
keyboard3.row("Вторник 2⃣", "Пятница 5⃣")
keyboard3.row("Среда 3⃣", "Суббота 6⃣")
keyboard3.row("Назад")
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row("Назад")
keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row("Ответить")
keyboard5.row("Назад")
torpl = [384161491]
textvspisok1 = []
textvspisok2 = []
textvspisok3 = []
textvspisok4 = []
textvspis = []
textvspisok5 = []
textvspisok6 = []
textvspisok7 = []
textdlspiska1 = "chtoto"
textdlspiska2 = "chtoto"
textdlspiska3 = "chtoto"
textdlspiska4 = "chtoto"
textdlspiska5 = "chtoto"
textdlspiska6 = "chtoto"
textdlspiska7 = "chtoto"
spisokbool = "false"
topost = [] 
nomer = 0
nomerrply = 0
rply = "false"
dorply = "false"
tehpod = "false"


    
@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id == 136502356:
        bot.send_message(message.chat.id, "Привет!) Я робот 10 «В» класса ✅.", )
        bot.send_message(message.chat.id, "<b>Здравствуй, создатель.</b>", reply_markup=keyboard1, parse_mode = "HTML")
        rply = "false"
        dorply = "false"
    else:
        bot.send_message(message.chat.id, "Привет!) Я робот 10 «В» класса ✅.", reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda callback:True)
def callback(callback):
    global torpl
    global spisokbool
    global textdlspiska1
    global textdlspiska2
    global textdlspiska3
    global textdlspiska4
    global textdlspiska5
    global textdlspiska6
    global textdlspiska7
    global topost
    global textvspisok1
    global textvspisok2
    global textvspisok3
    global textvspisok4
    global textvspisok5
    global textvspisok6
    global textvspisok7
    global nomer
    global rply
    global nomerrply
    global dorply
    global tehpod
    if callback.data == "QuestionsList":
        rply = "false"
        cancel = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text="Ответить", callback_data="Cancel")
        cancel.add(but_2)
        bot.send_message(callback.message.chat.id, "Сообщений: " + str(nomer) + "\nВыбери номер сообщения, которое хочешь посмотреть.", reply_markup=cancel )
        spisokbool = "true"
    if callback.data == "Cancel":
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Список сообщений", callback_data="QuestionsList")
        key.add(but_1)
        spisokbool = "false"
        rply = "true"    
        bot.send_message(callback.message.chat.id, 'Введи номер сообщения, на которое хочешь ответить.', reply_markup=key)
    
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, {' Я помогу вам разобраться.\n\nЧтобы узнать расписание\n- "Расписание 📋"\n\nЧтобы обратиться за помощью к создателю\n- "Тех. поддержка 📩" '}, reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global torpl
    global textdlspiska1
    global textdlspiska2
    global spisokbool
    global textdlspiska3
    global textdlspiska4
    global textdlspiska5
    global textdlspiska6
    global textdlspiska7
    global topost
    global textvspisok1
    global textvspisok2
    global textvspisok3
    global textvspisok4
    global textvspisok5
    global textvspisok6
    global textvspisok7
    global nomer
    global rply
    global nomerrply
    global dorply
    global tehpod
    if tehpod == "false":
        if message.text == 'Расписание 📋':
            bot.send_message(message.chat.id, 'Расписание:', reply_markup=keyboard2)
        if message.text == 'Назад':
            bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard1)
            rply = "false"
            dorply = "false"
            tehpod = "false"
            spisokbool = "false"
        if message.text == 'Уроки 📆':
            bot.send_message(message.chat.id, 'Выберите день недели.', reply_markup=keyboard3)
        if message.text == 'Звонки ⏰':
            bot.send_message(message.chat.id, 'Расписание звонков:\n\n1) 8:30-9:15 ✅\n2) 9:20-10:00 ☑️\n3) 10:05-10:45 ✅\n4) 10:55-11:35 ☑️\n5) 11:50-12:30 ✅\n6) 12:40-13:20 ☑\n\nС вами робот 10 "В" !', reply_markup=keyboard2) 
        if message.text == 'Понедельник 1⃣':
            bot.send_message(message.chat.id, '1) Русский язык ✅\n2) ДПЮ ☑️\n3) ЧО ✅\n4) Алгебра ☑️\n5) Всемирная история ✅', reply_markup=keyboard3)
        if message.text == 'Вторник 2⃣':
            bot.send_message(message.chat.id, '1) Английский язык / Узбекский язык ☑️\n2) Физика ✅\n3) Биология ☑️\n4) География ✅\n5) Английский язык / Узбекский язык ☑️', reply_markup=keyboard3)        
        if message.text == 'Среда 3⃣':
            bot.send_message(message.chat.id, '1) Алгебра ✅\n2) Химия ☑️\n3) История Узбекистана ✅\n4) Информатика / Узбекский язык ☑️\n5) Информатика / Узбекский язык ✅', reply_markup=keyboard3)
        if message.text == 'Четверг 4⃣':
            bot.send_message(message.chat.id, '1) Информатика / Узбекский язык ☑️\n2) Информатика / Узбекский язык ✅\n3) Химия ☑️\n4) Алгебра ✅\n5) Английский язык ☑️', reply_markup=keyboard3)
        if message.text == 'Пятница 5⃣':
            bot.send_message(message.chat.id, '1) ДПЮ / Физ-ра ✅\n2) Русский язык ☑️\n3) Физика ✅\n4) Биология ☑️\n5) История Религий ✅', reply_markup=keyboard3)
        if message.text == 'Суббота 6⃣':
            bot.send_message(message.chat.id, '1) Право ☑️\n2) Алгебра ✅\n3) Русский язык ☑️\n4) Физ-ра ✅\n5) Английский язык ☑️', reply_markup=keyboard3)       
    else: {}   
        
    if message.text == 'Тех. поддержка 📩': 
        if message.chat.id == 136502356:
            bot.send_message(message.chat.id, 'Тех. поддержка:', reply_markup=keyboard5)               
        else:
            bot.send_message(message.chat.id, 'Напишите нам.', reply_markup=keyboard4)
        tehpod = "true"
    if not message.text == 'Тех. поддержка 📩': 
        if tehpod == "true":
            if not message.chat.id == 136502356:
                if message.text == 'Назад':
                    bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard1)
                    rply = "false"
                    dorply = "false"
                    tehpod = "false"
                    spisokbool = "false"
                if not message.text == 'Назад':
                    bot.send_message(message.chat.id, "Сообщение отправлено, мы ответим вам в ближайшее время.", reply_markup=keyboard1)
                    torpl.append(message.chat.id)
                    nomer = nomer + 1   
                    bot.send_message("136502356", "<b> ------------------------- </b>", parse_mode = "HTML")
                    bot.send_message("136502356", "Сообщение: " + message.text ,) 
                    bot.send_message("136502356", "Id пользователя: " + str(message.chat.id),)
                    bot.send_message("136502356", "Имя пользователя: " + message.from_user.first_name,)
                    if message.from_user.username:
                        bot.send_message("136502356", "Аккаунт пользователя: " + "@" + message.from_user.username,)
                        textdlspiska5 = "Аккаунт пользователя: " + "@" + message.from_user.username
                    else:
                        bot.send_message("136502356", "Аккаунт пользователя: " + '<a href="tg://user?id='+str(message.from_user.id)+'">' + message.from_user.first_name + '</a>', parse_mode = "HTML")
                        textdlspiska5 = "Аккаунт пользователя: " + '<a href="tg://user?id='+str(message.from_user.id)+'">' + message.from_user.first_name + '</a>'
                    bot.send_message("136502356", "Номер сообщения: " + str(nomer),)
                    bot.send_message("136502356", "<b> ------------------------- </b>", parse_mode = "HTML")
                    textdlspiska1 = "<b> ------------------------- </b>"
                    textdlspiska2 = "Сообщение: " + message.text
                    textdlspiska3 = "Id пользователя: " + str(message.chat.id)
                    textdlspiska4 = "Имя пользователя: " + message.from_user.first_name
                    textdlspiska6 = "Номер сообщения: " + str(nomer)
                    textdlspiska7 = "<b> ------------------------- </b>"
                    textvspisok1.append(textdlspiska1)
                    textvspisok2.append(textdlspiska2)
                    textvspisok3.append(textdlspiska3)
                    textvspisok4.append(textdlspiska4)
                    textvspisok5.append(textdlspiska5)
                    textvspisok6.append(textdlspiska6)
                    textvspisok7.append(textdlspiska7)
                    print(nomer)
                    print(torpl)
                    print (textvspisok1)
                    print (textvspisok2)
                    print (textvspisok3)
                    print (textvspisok4)
                    print (textvspisok5)
                    print (textvspisok6)
                    print (textvspisok7)
                    tehpod = "false"
            else:
                if message.text == 'Ответить':
                    if not nomer == 0:
                        key = types.InlineKeyboardMarkup()
                        cancel = types.InlineKeyboardMarkup()
                        but_1 = types.InlineKeyboardButton(text="Список сообщений", callback_data="QuestionsList")
                        but_2 = types.InlineKeyboardButton(text="Ответить", callback_data="Cancel")
                        key.add(but_1)
                        cancel.add(but_2)
                        bot.send_message(message.chat.id, 'Введи номер сообщения, на которое хочешь ответить.', reply_markup=keyboard4)
                        bot.send_message(message.chat.id, 'Также ты можешь просмотреть список сообщений.', reply_markup=key)
                        rply = "true"
                    else:
                        bot.send_message(message.chat.id, "Новых сообщений нет", reply_markup=keyboard1)
                        tehpod = "false"
                if message.text == 'Назад':
                    bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard1)
                    rply = "false"
                    dorply = "false"
                    tehpod = "false"
                if not message.text == 'Ответить':
                    if rply == "true" :
                        if message.text.isdigit():
                            if not message.text == "0":
                                if message.text <= str(nomer):
                                    nomerrply = message.text
                                    bot.send_message(message.chat.id, 'Ты отвечаешь на сообщение под номером: ' + message.text + ", введи ответ.", reply_markup=keyboard4)
                                    dorply = "true"
                                    rply = "false"
                                else:
                                    bot.send_message(message.chat.id, 'Не существует сообщения с таким номером.', reply_markup=keyboard4)
                            else: {bot.send_message(message.chat.id, 'Не существует сообщения с таким номером.', reply_markup=keyboard4)}       
                        else:
                            bot.send_message(message.chat.id, 'Номер сообщения введен неверно.', reply_markup=keyboard4)
                if not message.text == nomerrply:      
                    if dorply == "true":
                        bot.send_message(message.chat.id, "Ответ отправлен.", reply_markup=keyboard1)
                        bot.send_message(torpl[int(nomerrply)], message.text,)
                        del torpl[int(nomerrply)]
                        del textvspisok1[int(nomerrply) - 1]
                        del textvspisok2[int(nomerrply) - 1]
                        del textvspisok3[int(nomerrply) - 1]
                        del textvspisok4[int(nomerrply) - 1]
                        del textvspisok5[int(nomerrply) - 1]
                        del textvspisok6[-1]
                        del textvspisok7[int(nomerrply) - 1]
                        nomer = nomer - 1
                        print(nomer)
                        print(torpl)
                        dorply = "false"
                        tehpod = "false"
                if spisokbool == "true" :
                    if message.text.isdigit():
                        if not message.text == "0":
                            if message.text <= str(nomer):
                                nomerrply = int(message.text) - 1
                                bot.send_message(message.chat.id, textvspisok1[int(nomerrply)], parse_mode="HTML")
                                bot.send_message(message.chat.id, textvspisok2[int(nomerrply)] )
                                bot.send_message(message.chat.id, textvspisok3[int(nomerrply)] )
                                bot.send_message(message.chat.id, textvspisok4[int(nomerrply)] )
                                bot.send_message(message.chat.id, textvspisok5[int(nomerrply)], parse_mode="HTML")
                                bot.send_message(message.chat.id, textvspisok6[int(nomerrply)] )
                                bot.send_message(message.chat.id, textvspisok7[int(nomerrply)], parse_mode="HTML")
                                key = types.InlineKeyboardMarkup()
                                but_1 = types.InlineKeyboardButton(text="Список сообщений", callback_data="QuestionsList")
                                key.add(but_1)
                                bot.send_message(message.chat.id, 'Введи номер сообщения, на которое хочешь ответить.', reply_markup=key)
                                spisokbool = "false"
                                rply = "true"
                            else:
                                bot.send_message(message.chat.id, 'Не существует сообщения с таким номером.', reply_markup=keyboard4)
                        else: {bot.send_message(message.chat.id, 'Не существует сообщения с таким номером.', reply_markup=keyboard4)}        
                    else:
                        bot.send_message(message.chat.id, 'Номер сообщения введен неверно.', reply_markup=keyboard4)

bot.polling()
