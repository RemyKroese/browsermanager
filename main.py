from core.browser_manager import BrowserManager
from core.config import Config
from gui.main_window import MainWindow


def main():
    config = Config()
    windows = config.read()
    browser_manager = BrowserManager(browser='firefox')
    gui = MainWindow(browser_manager, windows)
    browser_manager.open_startup_windows(windows)
    gui.show()
    gui.execute_app()


if __name__ == '__main__':
    main()
