from gen_user import gen_user
import pytest


@pytest.fixture
def phone():
    phone = gen_user.gen_phone()
    return phone


def test_return_string(phone):
    assert isinstance(phone, str)


def test_return_string_of_10_char(phone):
    print(phone)
    assert len(phone) == 10


def test_string_position_0_and_3_not_zero(phone):
    assert phone[0] != '0' and phone[3] != '0'


def test_string_position_0_not_one(phone):
    assert phone[0] != '1'
