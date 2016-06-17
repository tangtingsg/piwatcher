import logging
import os

LOG_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_logging():
    logging.basicConfig(
        level =logging.DEBUG,
        format = '%(levelname)s %(asctime)s %(filename)s[%(lineno)d] %(threadName)s : %(message)s',
        datefmt = '%m-%d %H:%M:%S',
        filename = os.path.join(LOG_DIR, 'temp.log'),
        filemode = 'a'
    )

