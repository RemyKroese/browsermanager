import mock

import browsermanager.browser as b


@mock.patch('subprocess.Popen')
def test_open_windows__one_window_with_one_tab(m_subprocess_Popen):
    test_window = ['url_1']
    b.open_windows([test_window])
    assert m_subprocess_Popen.call_count == 1


@mock.patch('subprocess.Popen')
def test_open_windows__one_window_with_multiple_tabs(m_subprocess_Popen):
    test_window = ['url_1', 'url_2']
    b.open_windows([test_window])
    assert m_subprocess_Popen.call_count == 2


@mock.patch('subprocess.Popen')
def test_open_windows__multiple_windows_with_multiple_tabs(m_subprocess_Popen):
    test_window = ['url_1', 'url_2']
    b.open_windows([test_window, test_window])
    assert m_subprocess_Popen.call_count == 4
