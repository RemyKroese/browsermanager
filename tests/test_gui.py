import mock
import pytest
from PyQt6 import QtCore

from browsermanager.gui import GUI


TEST_WINDOWS = [['b1_u1', 'b1_u2'], ['b2_u1', 'b2_u2', 'b2_u3']]


@pytest.fixture()
def gui():
    yield GUI(TEST_WINDOWS)


# TODO: Investigate access violation with @pytest.mark.parametrize

def test_gui__header_layout_is_loaded(gui):
    # TODO: investigate verifying elements in the layout
    elements = gui.window_elements['header_layouts']
    assert len(elements) == 2
    assert elements[0].isEnabled()
    assert elements[1].isEnabled()


def test_gui__header_is_loaded(gui):
    elements = gui.window_elements['headers']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].text() == 'window 1'
    assert elements[1].isEnabled() and elements[1].text() == 'window 2'


def test_gui__open_checkbox_is_loaded(gui):
    elements = gui.window_elements['open_checkboxes']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].isChecked()
    assert elements[1].isEnabled() and elements[1].isChecked()


def test_gui__open_button_is_loaded(gui):
    elements = gui.window_elements['open_buttons']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].text() == 'Open'
    assert elements[1].isEnabled() and elements[1].text() == 'Open'


def test_gui__list_widget_is_loaded(gui):
    elements = gui.window_elements['list_widgets']
    items1 = [elements[0].item(x).text() for x in range(elements[0].count())]
    items2 = [elements[1].item(x).text() for x in range(elements[1].count())]
    assert len(elements) == 2
    assert elements[0].isEnabled() and items1 == TEST_WINDOWS[0]
    assert elements[1].isEnabled() and items2 == TEST_WINDOWS[1]


@mock.patch('browsermanager.gui.GUI.open_window_clicked')
def test_open_button_clicked__calls_open_window_clicked(open_window_clicked, gui):
    gui.window_elements['open_buttons'][0].click()
    assert open_window_clicked.call_count == 1
# @mock.patch('browsermanager.gui.GUI.open_window_clicked')
# def test_open_button_clicked__calls_open_window_clicked(open_window_clicked, gui, qtbot):
#     qtbot.mouseClick(gui.window_elements['open_buttons'][0], QtCore.Qt.MouseButton.LeftButton)
#     assert open_window_clicked.call_count == 1


@mock.patch('PyQt6.QtWidgets.QWidget.show')
def test_show__calls_gui_show(show, gui):
    gui.show()
    assert show.call_count == 1


@mock.patch('PyQt6.QtWidgets.QApplication.exec')
def test_execute_app__calls_application_exec(exec, gui):
    gui.execute_app()
    assert exec.call_count == 1
