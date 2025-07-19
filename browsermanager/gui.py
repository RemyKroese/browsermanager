import os
import sys
from PyQt6 import QtWidgets
from screeninfo import get_monitors

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from browsermanager import browser  # noqa


class GUI():
    def __init__(self, windows):
        self.app = QtWidgets.QApplication([])
        self.gui = QtWidgets.QWidget()
        self.window_elements = {
            'header_layouts': [],
            'headers':        [],
            'open_checkboxes': [],
            'open_buttons':   [],
            'list_widgets':   [],
        }

        self.overview_layout = QtWidgets.QGridLayout()

        for i, window in enumerate(windows):
            header_layout = QtWidgets.QHBoxLayout()
            header = QtWidgets.QLabel(window['name'])
            header_layout.addWidget(header)

            open_checkbox = QtWidgets.QCheckBox("Open on startup")
            open_checkbox.setChecked(window['run_on_startup'])
            header_layout.addWidget(open_checkbox)

            open_button = QtWidgets.QPushButton('Open')
            open_button.clicked.connect(lambda clicked, w=window: self.open_window_clicked(w))
            header_layout.addWidget(open_button)

            list_widget = QtWidgets.QListWidget()
            for url in window['urls']:
                QtWidgets.QListWidgetItem(url, list_widget)
            self.overview_layout.addLayout(header_layout, 0, i)
            self.overview_layout.addWidget(list_widget, 1, i)

            self.window_elements['header_layouts'].append(header_layout)
            self.window_elements['headers'].append(header)
            self.window_elements['open_checkboxes'].append(open_checkbox)
            self.window_elements['open_buttons'].append(open_button)
            self.window_elements['list_widgets'].append(list_widget)

        self.gui.setLayout(self.overview_layout)

    def open_window_clicked(self, window):
        browser.open_window(window, 'firefox', sort_monitors_by_windows_order(get_monitors()))

    def show(self):
        self.gui.show()

    def execute_app(self):
        self.app.exec()


# TODO: refactor code structure
def sort_monitors_by_windows_order(monitors):
    # sort the list of displays by their windows display name (e.g. DISPLAY1, DISPLAY2)
    # string length sorting done too for the lunatics who have 10 or more displays
    return sorted(monitors, key=lambda m: (len(m.name), m.name))
