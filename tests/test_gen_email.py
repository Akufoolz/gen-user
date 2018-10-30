from gen_user import gen_user
import pytest


@pytest.fixture
def email():
    name = gen_user.gen_name()
    email = gen_user.gen_email(name)
    return email


def test_return_string(email):
    assert isinstance(email, str)


def test_email_contains_only_one_at_symbol(email):
    lst = email.split('@')
    if len(lst) == 2:
        assert True
    else:
        assert False


def test_email_contains_dot_after_at_symbol(email):
    lst = email.split('@')
    print(email)
    assert '.' in lst[1]
