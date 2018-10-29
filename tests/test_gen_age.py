from gen_user import gen_user
import pytest


@pytest.fixture
def age():
    age = gen_user.gen_age()
    return age


def test_returns_int(age):
    assert isinstance(age, int)


def test_returns_int_between_16_and_116(age):
    assert 16 <= age <= 116
