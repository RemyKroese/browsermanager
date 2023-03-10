import configparser
import os

config = configparser.ConfigParser()
CONFIG_PATH = 'config.ini'


def create():
    window = ['https://github.com/RemyKroese/browsermanager#readme']
    write([window])


def write(windows):
    for i, window in enumerate(windows):
        config.add_section('window_' + str(i+1))
        for j, url in enumerate(window):
            config['window_' + str(i+1)]['url_' + str(j+1)] = url
    with open(CONFIG_PATH, 'w') as config_file:
        config.write(config_file)


def read():
    if not os.path.isfile(CONFIG_PATH):
        create()
    config.read(CONFIG_PATH)
    windows = []
    for section in config.sections():
        windows.append(list(config[section].values()))
    return windows
