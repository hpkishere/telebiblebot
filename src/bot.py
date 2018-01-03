from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler
from commands import start, help_command, remindon, remindoff, retrieve, inline_retrieve, reminder_time_callback, github
import logging, token_secret

token = token_secret.token

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#entry point
def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    remindon_handler = CommandHandler('remindon', remindon)
    remindoff_handler = CommandHandler('remindoff', remindoff,
        pass_chat_data=True
    )
    retrieve_handler = CommandHandler('retrieve', retrieve,
        pass_args=True
    )
    help_handler = CommandHandler('help', help_command)
    inline_retrieve_handler = InlineQueryHandler(inline_retrieve)
    callback_query_handler = CallbackQueryHandler(reminder_time_callback,
        pass_job_queue=True,
        pass_chat_data=True
    )
    github_handler = CommandHandler('github', github)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(github_handler)
    dispatcher.add_handler(remindon_handler)
    dispatcher.add_handler(remindoff_handler)
    dispatcher.add_handler(retrieve_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(inline_retrieve_handler)
    dispatcher.add_handler(callback_query_handler)

    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
