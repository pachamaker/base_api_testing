import logging
from settings import ROOT_DIR


logger = logging.getLogger('root')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = logging.FileHandler('%s/autotests.log' % ROOT_DIR)
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


def log_error(message, raise_exception=False):
    logger.error(message)

    if raise_exception:
        raise ValueError(message)
