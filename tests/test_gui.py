from unittest import mock

from gui.main_window import MainWindow


TEST_WINDOWS = [
    {
        'name': 'window 1',
        'run_on_startup': True,
        'urls': ['a', 'b']
    },
    {
        'name': 'window 2',
        'run_on_startup': False,
        'urls': ['d', 'e']
    }
]
fake_browser_manager = mock.Mock()
main_window = MainWindow(fake_browser_manager, TEST_WINDOWS)


def test_gui__header_layout_is_loaded():
    # TODO: investigate verifying elements in the layout
    elements = main_window.window_elements['header_layouts']
    assert len(elements) == 2
    assert elements[0].isEnabled()
    assert elements[1].isEnabled()


def test_gui__header_is_loaded():
    elements = main_window.window_elements['headers']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].text() == 'window 1'
    assert elements[1].isEnabled() and elements[1].text() == 'window 2'


def test_gui__open_checkbox_is_loaded():
    elements = main_window.window_elements['open_checkboxes']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].isChecked()
    assert elements[1].isEnabled() and not elements[1].isChecked()


def test_gui__open_button_is_loaded():
    elements = main_window.window_elements['open_buttons']
    assert len(elements) == 2
    assert elements[0].isEnabled() and elements[0].text() == 'Open'
    assert elements[1].isEnabled() and elements[1].text() == 'Open'


def test_gui__list_widget_is_loaded():
    elements = main_window.window_elements['list_widgets']
    items1 = [elements[0].item(x).text() for x in range(elements[0].count())]
    items2 = [elements[1].item(x).text() for x in range(elements[1].count())]
    assert len(elements) == 2
    assert elements[0].isEnabled() and items1 == TEST_WINDOWS[0]['urls']
    assert elements[1].isEnabled() and items2 == TEST_WINDOWS[1]['urls']


def test_open_button_clicked__calls_open_window_clicked():
    main_window.window_elements['open_buttons'][0].click()
    assert fake_browser_manager.open_window.call_count == 1


@mock.patch('PyQt6.QtWidgets.QWidget.show')
def test_show__calls_gui_show(show):
    main_window.show()
    assert show.call_count == 1


@mock.patch('PyQt6.QtWidgets.QApplication.exec')
def test_execute_app__calls_application_exec(exec):
    main_window.execute_app()
    assert exec.call_count == 1
