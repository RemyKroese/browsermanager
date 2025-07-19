from unittest.mock import patch

import browsermanager.browser as b


@patch('browsermanager.browser.wait_for_new_window', return_value=True)
@patch('browsermanager.browser.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_one_tab(m_subprocess_Popen, m_position_windows, m_wait_for_new_window):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a']
        }
    ]
    b.open_startup_windows(test_windows, 'firefox', [''])
    assert m_subprocess_Popen.call_count == 1


@patch('browsermanager.browser.wait_for_new_window', return_value=True)
@patch('browsermanager.browser.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_multiple_tabs(m_subprocess_Popen, m_position_windows, m_wait_for_new_window):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a', 'b']
        }
    ]
    b.open_startup_windows(test_windows, 'chrome', [''])
    assert m_subprocess_Popen.call_count == 2


@patch('browsermanager.browser.wait_for_new_window', return_value=True)
@patch('browsermanager.browser.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_multiple_windows_with_multiple_tabs(m_subprocess_Popen, m_position_windows, m_wait_for_new_window):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a', 'b']
        },
        {
            'name': 'window_2',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['d', 'e']
        }
    ]
    b.open_startup_windows(test_windows, '', [''])
    assert m_subprocess_Popen.call_count == 4


@patch('browsermanager.browser.wait_for_new_window', return_value=True)
@patch('browsermanager.browser.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__window_not_opened_when_run_on_startup_is_false(m_subprocess_Popen, m_position_windows, m_wait_for_new_window):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': False,
            'urls': ['a', 'b']
        }
    ]
    b.open_startup_windows(test_windows, '', [''])
    assert m_subprocess_Popen.call_count == 0
