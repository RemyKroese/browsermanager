
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from browsermanager import browser        # noqa
from browsermanager.config import Config  # noqa
from browsermanager.gui import GUI        # noqa


def main():
    config = Config()
    windows = config.read()
    gui = GUI(windows)
    gui.show()
    browser.open_windows(windows)
    gui.execute_app()


if __name__ == '__main__':
    main()
