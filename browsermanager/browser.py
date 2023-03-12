import subprocess
import time

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def open_startup_windows(windows):
    for window in windows:
        if window['run_on_startup']:
            open_window(window)


def open_window(window):
    urls = window['urls']
    subprocess.Popen([CHROME_PATH, urls[0], '--new-window'])
    time.sleep(1)
    for i in range(1, len(urls)):
        subprocess.Popen([CHROME_PATH, urls[i]])
        time.sleep(0.1)
