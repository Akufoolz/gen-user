from gen_user import gen_user


def test_list_length_equals_3():
    lst = gen_user.multi_rand(0, 9, 3)
    assert len(lst) == 3


def test_list_length_equals_32():
    lst = gen_user.multi_rand(0, 9, 32)
    assert len(lst) == 32
