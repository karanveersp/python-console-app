from my_python_app import __version__, util


def test_version():
    assert __version__ == "0.1.0"


def test_util_has_func():
    assert util.utilfunc is not None
