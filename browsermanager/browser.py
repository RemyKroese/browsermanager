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
    elif browser == 'chrome':
        browser_path = CHROME_PATH
    else:
        browser_path = 'explorer'

    urls = window['urls']
    before = get_window_handles()
    subprocess.Popen([browser_path, '--new-window', urls[0]])
    ff_window = wait_for_new_window(before)
    position_window(ff_window, monitors[window['monitor']-1])
    for url in urls[1:]:
        subprocess.Popen([browser_path, url])
        time.sleep(0.5)


def get_hwnd(win):
    """
    Safely retrieves the HWND (handle to a window) from a pygetwindow.Window object.

    _hWnd is a Windows-specific identifier (HWND) that uniquely identifies a window.
    pygetwindow exposes it internally via the _hWnd attribute.
    """
    return getattr(win, '_hWnd', None)


def get_window_handles():
    """
    Returns a set of handles (_hWnd) for all currently visible windows.
    """
    return set(get_hwnd(win) for win in gw.getAllWindows() if win.visible)


def wait_for_new_window(before, timeout=5, check_interval=0.1):
    """
    Waits for a new visible window to appear that wasn't in the 'before' set.
    """
    checks = int(timeout / check_interval)
    for _ in range(checks):
        new_handles = get_window_handles() - before
        for win in gw.getAllWindows():
            if get_hwnd(win) in new_handles and win.visible:
                return win
        time.sleep(check_interval)
    raise TimeoutError(f'No new window appeared within {timeout} seconds.')


def position_window(window, monitor):
    """
    Moves and resizes the given window to match the specified monitor's geometry.
    """
    window.moveTo(monitor.x, monitor.y)
    window.resizeTo(monitor.width, monitor.height)
