from gen_user import gen_user
import pytest


@pytest.fixture
def name():
    string = gen_user.gen_name()
    return string


def test_return_string(name):
    assert isinstance(name, str)


def test_return_non_empty_string(name):
    assert len(name) != 0


def test_return_first_and_last_name(name):
    print(name)
    assert len(name) > 2 and (' ' in name)
