from gen_user import gen_user


def test_return_string():
    string = gen_user.build_name()
    assert isinstance(string, str)


def test_return_non_empty_string():
    string = gen_user.build_name()
    assert len(string) != 0


def test_return_first_and_last_name():
    string = gen_user.build_name()
    assert len(string) > 2 and (' ' in string)
