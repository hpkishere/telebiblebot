from telegram import InlineKeyboardButton

reminder_verses = [
    '<b>Isaiah 40:31</b> \n\n but those who hope in the LORD will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.',
    '<b>Joshua 1:8</b> \n\n Keep this Book of the Law always on your lips; meditate on it day and night, so that you may be careful to do everything written in it. Then you will be prosperous and successful.',
    '<b>1 Chronicles</b> 16:11 \n\n Look to the LORD and his strength; seek his face always.'
]

help_msg = 'List of available commands \n\n /remindon To set a daily reminder to hear God\'s words! \n /remindoff To turn off reminder feature \n /retrieve <book> <chapter>:<verse> To retrieve bible verses, verse is optional and can be a range \n\n Example: \n /retrieve Genesis 1:2 \n /retrieve Genesis 1:1-2 \n /retrieve Genesis 1:1-2,4-5,7 \n /retrieve Genesis 1 \n \n /help To list all commands. \n\n Are you a developer? \n /github for source code'

github_link = 'https://github.com/hpkishere/telebiblebot'

keyboard = [
                [
                    InlineKeyboardButton("3AM", callback_data='1'),
                    InlineKeyboardButton("6AM", callback_data='2')
                ],
                [
                    InlineKeyboardButton("9AM", callback_data='3'),
                    InlineKeyboardButton("12PM", callback_data='4')
                ],
                [
                    InlineKeyboardButton("3PM", callback_data='5'),
                    InlineKeyboardButton("6PM", callback_data='6')
                ],
                [
                    InlineKeyboardButton("9PM", callback_data='7'),
                    InlineKeyboardButton("12AM", callback_data='8'),
                ],
           ]