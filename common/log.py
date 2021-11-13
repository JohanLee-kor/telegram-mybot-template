import logging
import logging.handlers
import sys

from common import utils

LOGGER_NAME = 'mybot'

app_name = utils.safe_list_get(sys.argv, 1, 'nan')
LOGGER_FILE_PATH = "./%s_%s.log" % (LOGGER_NAME, app_name)
LOG_FILE_MAX_BYTES = 100 * 1024 * 1024  # 100MB
LOG_FILE_BACKUP_COUNT = 5
FMT = logging.Formatter('%(asctime)s | %(levelname)s | [%(filename)s:%(funcName)20s():%(lineno)d] |  - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(FMT)

log = logging.getLogger(LOGGER_NAME)
log.setLevel(logging.DEBUG)
log.addHandler(stream_handler)


def set_logger(log_file_name: str, log_level: int):
    handler = logging.handlers.RotatingFileHandler(log_file_name,
                                                   maxBytes=LOG_FILE_MAX_BYTES,
                                                   backupCount=LOG_FILE_BACKUP_COUNT)
    handler.setFormatter(FMT)
    log.addHandler(handler)
    log.setLevel(log_level)


set_logger(LOGGER_FILE_PATH, logging.DEBUG)
log.debug('LOG LEVEL DEBUG')
log.info('LOG LEVEL INFO')
log.warning('LOG LEVEL WARNING')
log.error('LOG LEVEL ERROR')
