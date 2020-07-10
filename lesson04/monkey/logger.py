

import logging

logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                filename='agent.log',
                filemode='a'
                )


logging.debug('hello world')
logging.info('hello world')
