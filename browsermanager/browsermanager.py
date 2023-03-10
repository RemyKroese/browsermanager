import subprocess
import time

import config

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def load_windows(windows):
    for window in windows:
        subprocess.Popen([CHROME_PATH, window[0], '--new-window'])
        time.sleep(1)
        for i in range(1, len(window)):
            subprocess.Popen([CHROME_PATH, window[i]])
            time.sleep(0.1)


def main():
    windows = config.read()
    load_windows(windows)


if __name__ == '__main__':
    main()
