import mock

import browsermanager.browser as b


@mock.patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_one_tab(m_subprocess_Popen):
    test_windows = [
        {
            'name': 'window_1',
            'run_on_startup': True,
            'urls': ['a']
        }
    ]
    b.open_startup_windows(test_windows, 'firefox')
    assert m_subprocess_Popen.call_count == 1


@mock.patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_multiple_tabs(m_subprocess_Popen):
    test_windows = [
        {
            'name': 'window_1',
            'run_on_startup': True,
            'urls': ['a', 'b']
        }
    ]
    b.open_startup_windows(test_windows, 'chrome')
    assert m_subprocess_Popen.call_count == 2


@mock.patch('subprocess.Popen')
def test_open_startup_windows__open_multiple_windows_with_multiple_tabs(m_subprocess_Popen):
    test_windows = [
        {
            'name': 'window_1',
            'run_on_startup': True,
            'urls': ['a', 'b']
        },
        {
            'name': 'window_2',
            'run_on_startup': True,
            'urls': ['d', 'e']
        }
    ]
    b.open_startup_windows(test_windows, '')
    assert m_subprocess_Popen.call_count == 4


@mock.patch('subprocess.Popen')
def test_open_startup_windows__window_not_opened_when_run_on_startup_is_false(m_subprocess_Popen):
    test_windows = [
        {
            'name': 'window_1',
            'run_on_startup': False,
            'urls': ['a', 'b']
        }
    ]
    b.open_startup_windows(test_windows, '')
    assert m_subprocess_Popen.call_count == 0
