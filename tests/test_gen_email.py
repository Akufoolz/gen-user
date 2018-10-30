from gen_user import gen_user
import pytest


@pytest.fixture
def email():
    email = gen_user.gen_email()
    return email


def test_return_string(email):
    assert isinstance(email, str)
