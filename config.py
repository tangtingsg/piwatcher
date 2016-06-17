import os
import configparser

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(PROJECT_DIR, 'config.ini')


def get_uuid():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'UUID' in config['DEFAULT']:
        return config['DEFAULT']['UUID']
    else:
        return ""


def get_psw():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'PSW' in config['DEFAULT']:
        return config['DEFAULT']['PSW']
    else:
        return ""


def get_uuid_psw():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    result = {'UUID': '', 'PSW': ''}
    if 'UUID' in config['DEFAULT']:
        result['UUID'] = config['DEFAULT']['UUID']
    if 'PSW' in config['DEFAULT']:
        result['PSW'] = config['DEFAULT']['PSW']
    return result


def get_identity_path():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'IDENTITY_PATH' in config['DEFAULT']:
        return config['DEFAULT']['IDENTITY_PATH']
    else:
        return ""


def set_uuid_psw(uuid, psw):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    config['DEFAULT']['UUID'] = uuid
    config['DEFAULT']['PSW'] = psw
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

