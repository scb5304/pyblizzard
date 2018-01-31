import configparser
import os

# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(__location__, 'config.ini'))


def get_api_key():
    return config['BLIZZARD']['key']

