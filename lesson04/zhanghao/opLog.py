import logging


def opLog():
    log_name = "access.log"
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    fh = logging.FileHandler(log_name)
    fmt = logging.Formatter(
        '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
