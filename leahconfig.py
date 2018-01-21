import configparser
config = configparser.ConfigParser()
config.read('config.ini')


def get_api_key():
    return config['BLIZZARD']['key']

