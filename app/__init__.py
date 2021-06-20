import logging


logging.basicConfig(filename="./logs/app_logs.log", format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
