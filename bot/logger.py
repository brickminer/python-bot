import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
FILENAME = 'bot.log'

logging.basicConfig(filename=FILENAME, format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)
