import logging
import os
class LogGen:


    @staticmethod
    def loggen():
        #logging.basicConfig(filename=".\\automation.log",
        #                   encoding='utf-8',
        #              format='%(asctime)s: %(levelname)s: %(message)s',
        #                datefmt='%m%d%Y %I:%M:%S %p')
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger=logging.getLogger()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger