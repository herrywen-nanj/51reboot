import logging


class Log(object):
    def opLog(self):
        logname = "access.log"
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        fh = logging.FileHandler(logname)
        fmt = logging.Formatter(
            '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
        fh.setFormatter(fmt)
        logger.addHandler(fh)
        return logger
