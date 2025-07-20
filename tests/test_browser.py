import pytest
from unittest.mock import patch

from core.browser_manager import BrowserManager


@pytest.fixture
def browser_manager():
    return BrowserManager('chrome')


@patch('core.browser_manager.BrowserManager.wait_for_new_window', return_value=True)
@patch('core.browser_manager.BrowserManager.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_one_tab(m_subprocess_Popen, m_position_windows, m_wait_for_new_window, browser_manager):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a']
        }
    ]
    browser_manager.open_startup_windows(test_windows)
    assert m_subprocess_Popen.call_count == 1


@patch('core.browser_manager.BrowserManager.wait_for_new_window', return_value=True)
@patch('core.browser_manager.BrowserManager.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_one_window_with_multiple_tabs(m_subprocess_Popen, m_position_windows, m_wait_for_new_window, browser_manager):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a', 'b']
        }
    ]
    browser_manager.open_startup_windows(test_windows)
    assert m_subprocess_Popen.call_count == 2


@patch('core.browser_manager.BrowserManager.wait_for_new_window', return_value=True)
@patch('core.browser_manager.BrowserManager.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__open_multiple_windows_with_multiple_tabs(m_subprocess_Popen, m_position_windows, m_wait_for_new_window, browser_manager):
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
    browser_manager.open_startup_windows(test_windows)
    assert m_subprocess_Popen.call_count == 4


@patch('core.browser_manager.BrowserManager.wait_for_new_window', return_value=True)
@patch('core.browser_manager.BrowserManager.position_window')
@patch('subprocess.Popen')
def test_open_startup_windows__window_not_opened_when_run_on_startup_is_false(m_subprocess_Popen, m_position_windows, m_wait_for_new_window, browser_manager):
    test_windows = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': False,
            'urls': ['a', 'b']
        }
    ]
    browser_manager.open_startup_windows(test_windows)
    assert m_subprocess_Popen.call_count == 0
