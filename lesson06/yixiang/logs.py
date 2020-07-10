import logging

fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
filename = './log/homework01_user_manager.log'

logging.basicConfig(level=logging.DEBUG,
                    format=fmt,
                    filename=filename,
                    filemode='w+',
                    datefmt='%a, %d %b %Y %H:%M:%S')

console = logging.StreamHandler()

console.setLevel(logging.DEBUG)  # 设置控制台日志输出的级别。如果设置为logging.INFO，就不会输出DEBUG日志信息

formatter = logging.Formatter(fmt)

console.setFormatter(formatter)

logging.getLogger().addHandler(console)


def info(msg):
    logging.info(msg)


def warning(msg):
    logging.warning(msg)


def error(msg):
    logging.error(msg)


