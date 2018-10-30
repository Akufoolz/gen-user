from gen_user import gen_user
import pytest


@pytest.fixture
def user():
    new_user = gen_user.gen_new_user()
    return new_user


def test_returns_dictionary(user):
    assert isinstance(user, dict)


def test_returns_dictionary_with_length_of_five(user):
    print(user)
    assert len(user) == 5
