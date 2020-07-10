import logging

def logger(data):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='./logs/agent.log',
                        filemode='a'
                        )
    logging.debug(data)
    msg = '日志写入成功'
    return msg