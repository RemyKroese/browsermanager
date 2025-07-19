
import os
import sys
from screeninfo import get_monitors

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from browsermanager import browser        # noqa
from browsermanager.config import Config  # noqa
from browsermanager.gui import GUI        # noqa


def main():
    config = Config()
    windows = config.read()
    gui = GUI(windows)
    monitors = sort_monitors_by_windows_order(get_monitors())
    browser.open_startup_windows(windows, browser='firefox', monitors=monitors)
    gui.show()
    gui.execute_app()


def sort_monitors_by_windows_order(monitors):
    # sort the list of displays by their windows display name (e.g. DISPLAY1, DISPLAY2)
    # string length sorting done too for the lunatics who have 10 or more displays
    return sorted(monitors, key=lambda m: (len(m.name), m.name))


if __name__ == '__main__':
    main()
