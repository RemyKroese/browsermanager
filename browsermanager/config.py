import configparser
import os


class Config():
    def __init__(self, config_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config_path = config_path
        if not os.path.isfile(self.config_path):
            new_window = ['https://github.com/RemyKroese/browsermanager#readme']
            self.write([new_window])

    def write(self, windows):
        for i, window in enumerate(windows):
            self.config.add_section('window_' + str(i+1))
            for j, url in enumerate(window):
                self.config['window_' + str(i+1)]['url_' + str(j+1)] = url
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    def read(self):
        self.config.read(self.config_path)
        windows = []
        for section in self.config.sections():
            windows.append(list(self.config[section].values()))
        return windows
