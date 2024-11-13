import logging

class FileLogger:

    def __init__(self, filename='output.txt'):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s',
            filename=filename,
            filemode='w'
        )
        self.logger = logging.getLogger('FileSystem')

    def log(self, message: str):
        self.logger.info(message)
