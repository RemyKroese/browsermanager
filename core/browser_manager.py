import subprocess
import time
from screeninfo import get_monitors
import pygetwindow as gw


CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FIREFOX_PATH = r'C:\Program Files\Mozilla Firefox\firefox.exe'


class BrowserManager():
    def __init__(self, browser):
        self.monitors = self._get_monitors_by_windows_order()
        self.browser_path = self._get_browser_path(browser)

    def _get_browser_path(self, browser):
        if browser == 'firefox':
            return FIREFOX_PATH
        elif browser == 'chrome':
            return CHROME_PATH
        else:
            return 'explorer'

    def _get_monitors_by_windows_order(self):
        monitors = get_monitors()
        # sort the list of displays by their windows display name (e.g. DISPLAY1, DISPLAY2)
        # string length sorting done too for the lunatics who have 10 or more displays
        return sorted(monitors, key=lambda m: (len(m.name), m.name))

    def _get_hwnd(self, win):
        """
        Safely retrieves the HWND (handle to a window) from a pygetwindow.Window object.

        _hWnd is a Windows-specific identifier (HWND) that uniquely identifies a window.
        pygetwindow exposes it internally via the _hWnd attribute.
        """
        return getattr(win, '_hWnd', None)

    def _get_window_handles(self, ):
        """
        Returns a set of handles (_hWnd) for all currently visible windows.
        """
        return set(self._get_hwnd(win) for win in gw.getAllWindows() if win.visible)

    def open_startup_windows(self, windows):
        for window in windows:
            if window['run_on_startup']:
                self.open_window(window)

    def open_window(self, window):
        urls = window['urls']
        before = self._get_window_handles()
        subprocess.Popen([self.browser_path, '--new-window', urls[0]])
        ff_window = self.wait_for_new_window(before)
        self.position_window(ff_window, self.monitors[window['monitor']-1])
        for url in urls[1:]:
            subprocess.Popen([self.browser_path, url])
            time.sleep(0.5)

    def wait_for_new_window(self, before, timeout=5, check_interval=0.1):
        """
        Waits for a new visible window to appear that wasn't in the 'before' set.
        """
        checks = int(timeout / check_interval)
        for _ in range(checks):
            new_handles = self._get_window_handles() - before
            for win in gw.getAllWindows():
                if self._get_hwnd(win) in new_handles and win.visible:
                    return win
            time.sleep(check_interval)
        raise TimeoutError(f'No new window appeared within {timeout} seconds.')

    def position_window(self, window, monitor):
        """
        Moves and resizes the given window to match the specified monitor's geometry.
        """
        window.moveTo(monitor.x, monitor.y)
        window.resizeTo(monitor.width, monitor.height)
