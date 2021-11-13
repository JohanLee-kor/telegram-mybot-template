from common.log import log
from model import chat


def do(bot, update):
    log.debug('start command <<<<<')
    chat_item = update.message.chat
    chat.create_chat(chat_item.id, chat_item.username, chat_item.first_name, chat_item.last_name)
