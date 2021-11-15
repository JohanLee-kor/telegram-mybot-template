# coding=utf-8
import telegram.ext
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters  # import modules


def error(update, context):
    """Log Errors caused by Updates."""
    print("update {} cased error: {}".format(update, context))


def add_commands(dispatcher: telegram.ext.Dispatcher):
    import command
    dispatcher.add_handler(CommandHandler('help', command.help.do))
    dispatcher.add_handler(CommandHandler('start', command.start.do))
    # 추가 Command 등록
    dispatcher.add_handler(MessageHandler(Filters.command, command.unknown))


def run_bot():
    import settings
    import message
    from common.log import log

    my_token = settings.conf['token']
    log.debug('>>>>>>>>>TELEGRAM BOT START>>>>>>>>>>>')

    updater = Updater(my_token, use_context=True)
    # message 처리 등록
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message.handling,
                                                  pass_chat_data=True,
                                                  pass_job_queue=True,
                                                  pass_update_queue=True,
                                                  pass_user_data=True))

    # Command 처리 등록
    add_commands(updater.dispatcher)

    updater.dispatcher.add_error_handler(error)

    updater.start_polling(timeout=1.5, clean=True)
    updater.idle()


def main():
    run_bot()


if __name__ == '__main__':
    main()
