
import filecmp
import os

from core.config import Config

ASSETS = os.path.join(os.path.dirname(__file__), 'assets/')


def test_config__init__create_basic_config_file_if_none_exists(tmp_path):
    expected_config_file = ASSETS + 'new_config.ini'
    new_config_file = tmp_path / 'config.ini'
    os.chdir(tmp_path)
    Config()
    assert os.path.exists(new_config_file)
    assert filecmp.cmp(new_config_file, expected_config_file)


def test_config__init__keep_config_file_if_one_exists(tmp_path):
    empty_config_file = (tmp_path / 'config.ini')
    empty_config_file.touch()
    os.chdir(tmp_path)
    Config()
    assert os.stat(empty_config_file).st_size == 0


def test_config__read_config_file():
    expected_result = [
        {
            'name': 'window_1',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['a', 'b', 'c']
        },
        {
            'name': 'window_2',
            'monitor': 2,
            'run_on_startup': False,
            'urls': ['d', 'e']
        },
        {
            'name': 'test_window_name',
            'monitor': 1,
            'run_on_startup': True,
            'urls': ['f', 'g']
        },
    ]

    os.chdir(ASSETS)
    config = Config()
    result = config.read()
    assert expected_result == result
