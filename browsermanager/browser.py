import subprocess
import time

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def open_windows(windows):
    for window in windows:
        open_window(window)


def open_window(window):
    subprocess.Popen([CHROME_PATH, window[0], '--new-window'])
    time.sleep(1)
    for i in range(1, len(window)):
        subprocess.Popen([CHROME_PATH, window[i]])
        time.sleep(0.1)
