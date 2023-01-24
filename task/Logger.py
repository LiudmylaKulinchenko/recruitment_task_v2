import logging
import os
from logging import Logger


class Logging(Logger):
    """Log data with timestamp to the file and to another AllLogs.log file"""

    LOGS_FILE = "AllLogs.log"
    LOGS_DIR = "logs"
    LOGGER_NAME = "task"

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

        self.file_name = file_name
        self.logger = self.create_logger(self.LOGGER_NAME)

    def create_logger(self, logger_name: str) -> logging.Logger:
        logger = logging.getLogger(name=logger_name)
        logger.setLevel("DEBUG")

        self.add_filehandler(logger=logger, file_name=self.LOGS_FILE, level="INFO")
        self.add_filehandler(logger=logger, file_name=self.file_name, level="INFO")

        return logger

    @staticmethod
    def add_formatter(filehandler: logging.FileHandler) -> None:
        formatter = logging.Formatter(
            fmt="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M:%S"
        )
        filehandler.setFormatter(formatter)

    def add_filehandler(
        self, logger: logging.Logger, file_name: str, level: str
    ) -> None:
        if not os.path.exists(self.LOGS_DIR):
            os.mkdir(self.LOGS_DIR)

        filehandler = logging.FileHandler(filename=os.path.join(self.LOGS_DIR, file_name))
        filehandler.setLevel(level=level)

        self.add_formatter(filehandler=filehandler)

        logger.addHandler(hdlr=filehandler)
