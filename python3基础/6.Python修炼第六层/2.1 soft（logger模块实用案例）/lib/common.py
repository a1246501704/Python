from conf import settings
import logging.config
import logging
import json

def conn_db(charset='utf-8'):
    dic=json.load(open(settings.DB_PATH,encoding=charset))
    return dic


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger=logging.getLogger(name)
    # logger=logging.getLogger('core.src')
    return logger