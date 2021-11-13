from datetime import datetime
from common.log import log
from settings import db

chat = db.get_collection('chat')


def create_chat(chat_id, username, first_name, last_name):
    """
    save chat info(bot member)
    """
    chat_item = {"chat_id": chat_id, "username": username, "first_name": first_name, "last_name": last_name,
                 "created_at": datetime.today()}

    log.debug('chat: %s' % chat_item)

    chat.insert_one(chat_item)
