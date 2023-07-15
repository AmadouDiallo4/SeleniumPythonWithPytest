import logging
import os
class LogGen:


    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter("%(asctime)s: - %(levelname)s: - %(name)s - :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger