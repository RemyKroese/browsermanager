import subprocess
import time

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FIREFOX_PATH = r'C:\Program Files\Mozilla Firefox\firefox.exe'


def open_startup_windows(windows, browser):
    for window in windows:
        if window['run_on_startup']:
            open_window(window, browser)


def open_window(window, browser):
    if browser == 'firefox':
        browser_path = FIREFOX_PATH
    elif browser == 'chrome':
        browser_path = CHROME_PATH
    else:
        browser_path = 'explorer'
    urls = window['urls']
    subprocess.Popen([browser_path, '--new-window', urls[0]])
    time.sleep(1)
    for i in range(1, len(urls)):
        subprocess.Popen([browser_path, urls[i]])
        time.sleep(0.2)
