from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, time
from helper_methods import alarm, http_request
import requests, variables

help_msg = variables.help_msg
keyboard = variables.keyboard
github_link = variables.github_link
reminded = False

#on bot start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi, I have started :)")
    bot.send_message(chat_id=update.message.chat_id, text=help_msg)

#on /help
def help_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=help_msg)

#on /github
def github(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=github_link)

#callback method from /remindon
def reminder_time_callback(bot, update, chat_data, job_queue):
    global reminded
    keyboard_query = update.callback_query
    
    #add a job to the job_queue based on time input by the user

    if keyboard_query.data == '1':
        t = time(3, 00, 00)
    elif keyboard_query.data == '2':
        t = time(6, 00, 00)
    elif keyboard_query.data == '3':
        t = time(9, 00, 00)
    elif keyboard_query.data == '4':
        t = time(12, 00, 00)
    elif keyboard_query.data == '5':
        t = time(15, 00, 00)
    elif keyboard_query.data == '6':
        t = time(18, 00, 00)
    elif keyboard_query.data == '7':
        t = time(21, 00, 00)
    elif keyboard_query.data == '8':
        t = time(00, 00, 00)
    
    chat_id=keyboard_query.message.chat_id
    message_id=keyboard_query.message.message_id
    
    context_array = [chat_id]
    job = job_queue.run_daily(alarm, t, context=context_array)
    chat_data['job'] = job
    
    bot.edit_message_text(text="OK! Will remind you to read your bible at " + str(t) + " daily! Do /remindoff to turn this off!",
                        chat_id=chat_id,
                        message_id=message_id)
    reminded = True

#on /remindon
def remindon(bot, update):
    global reminded
    if reminded == False :
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please choose your reminder timing:', reply_markup=reply_markup)

    else :
        update.message.reply_text("Remind feature is already turned on!")

#on /remindoff
def remindoff(bot, update, chat_data):
    global reminded
    if reminded == False :
        update.message.reply_text('Remind feature is not on! Do /remindon to turn it on')
        return
    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Remind feature is now turned off!')
    reminded = False

#on /retrieve
def retrieve(bot, update, args):
    try:
        book = args[0]
        chapterverse = args[1]
        
        message = http_request(book, chapterverse)

        #to consider for telegram message max length (4096 char)
        if len(message) <= 4095 :
            bot.send_message(parse_mode='HTML', chat_id=update.message.chat_id, text=message)
        else :
            split_msg_list = []
            while message:
                split_msg_list.append(message[:4095])
                message = message[4095:]
            
            for a in range(0, len(split_msg_list)):
                bot.send_message(parse_mode='HTML', chat_id=update.message.chat_id, text=split_msg_list[a])

    except (IndexError, ValueError, requests.exceptions.HTTPError):
        update.message.reply_text("Sorry, that is an invalid input :(, /retrieve <book> <chapter>:<verse>")

#on inline retrieve
def inline_retrieve(bot, update):
    query = update.inline_query.query
    if not query:
        return

    query_split = query.split()
    book = query_split[0]
    chapterverse = query_split[1]

    message = http_request(book, chapterverse)
    
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query,
            title=query,
            input_message_content=InputTextMessageContent(parse_mode='HTML', message_text=message)
        )
    )

    bot.answer_inline_query(update.inline_query.id, results)
