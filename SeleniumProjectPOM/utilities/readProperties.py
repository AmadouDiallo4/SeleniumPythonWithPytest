import configparser
import os
config = configparser.RawConfigParser()
ROOT_DIR = "Configurations"
config_path = os.path.join(ROOT_DIR, "config.ini")
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password