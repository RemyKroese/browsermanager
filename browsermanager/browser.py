import subprocess
import time
import pygetwindow as gw

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FIREFOX_PATH = r'C:\Program Files\Mozilla Firefox\firefox.exe'


def open_startup_windows(windows, browser, monitors):
    for window in windows:
        if window['run_on_startup']:
            open_window(window, browser, monitors)


def open_window(window, browser, monitors):
    if browser == 'firefox':
        browser_path = FIREFOX_PATH
        title_match = 'Mozilla Firefox'
    elif browser == 'chrome':
        browser_path = CHROME_PATH
        title_match = 'Google Chrome'
    else:
        browser_path = 'explorer'
        title_match = ''  # fallback

    urls = window['urls']
    before = [w for w in gw.getWindowsWithTitle(title_match) if w.visible]
    subprocess.Popen([browser_path, '--new-window', urls[0]])
    ff_window = wait_for_new_window(before, title_match)
    position_window(ff_window, monitors[window['monitor']-1])
    for i in range(1, len(urls)):
        subprocess.Popen([browser_path, urls[i]])
        time.sleep(0.5)


def wait_for_new_window(before, title_contains, timeout=5, check_interval=0.1):
    checks = int(timeout / check_interval)
    for _ in range(checks):
        after = [w for w in gw.getWindowsWithTitle(title_contains) if w.visible]
        new_windows = [w for w in after if w not in before]
        if new_windows:
            return new_windows[0]
        time.sleep(check_interval)
    raise TimeoutError(f'No new window appeared within {timeout} seconds.')


def position_window(window, monitor):
    window.moveTo(monitor.x, monitor.y)
    window.resizeTo(monitor.width, monitor.height)
