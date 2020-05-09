import logging


class Logger():
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    FILENAME = 'bot.log'

    def __init__(self, filename=FILENAME, level=logging.DEBUG, format=FORMAT):
        self.filename = filename
        self.level = level
        self.format = format

    def getLogger(self):
        logging.basicConfig(filename=self.filename,
                            level=self.level,
                            format=self.format)
        return logging.getLogger(__name__)
