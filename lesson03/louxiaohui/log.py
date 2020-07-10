#!/usr/bin/env python
import logging, os, re
from logging.handlers import TimedRotatingFileHandler

BASEPATH = os.path.realpath(os.path.dirname(__file__))
LOGPATH = BASEPATH + os.sep + 'log'
LOGFILE = LOGPATH + os.sep + 'app.log'
os.makedirs(LOGPATH,mode=0o644,exist_ok=False)

def Write_to_Log():
    log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        # create formatter
    formatter = logging.Formatter(log_fmt)
    formatter.datefmt = '%d/%b/%Y %H:%M:%S'
        
    # create log_file_handler
    log_file_handler = TimedRotatingFileHandler(
                       filename=LOGFILE, when="midnight", interval=1, backupCount=30)
    log_file_handler.suffix = "%Y-%m-%d.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    # create logger named log 
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    # add log_file_handler to logger
    log.addHandler(log_file_handler)
    return log

log = Write_to_Log()

log.info('This will get logged')
log.debug('This will get logged')
log.critical('This will get logged')
log.warning('This will get logged')
log.error('This will get logged')

