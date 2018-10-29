from gen_user import gen_user


def test_list_length_3():
    lst = gen_user.multi_rand(0, 9, 3)
    assert len(lst) == 3
