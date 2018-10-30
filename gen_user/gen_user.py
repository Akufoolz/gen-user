from random import randint


def syllables():
    syl_list = [
            'a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa',
            'i', 'ki', 'shi', 'chi', 'ni', 'hi', 'mi', 'ri', 'wi',
            'u', 'ku', 'su', 'tsu', 'nu', 'fu', 'mu', 'yu', 'ru',
            'e', 'ke', 'se', 'te', 'ne', 'he', 'me', 're', 'we',
            'o', 'ko', 'so', 'to', 'no', 'ho', 'mo', 'yo', 'ro', 'wo'
            ]
    return syl_list


def email_providers():
    lst = [
        'gmail.com', 'outlook.com', 'yahoo.com',
        'protonmail.com', 'icloud.com'
        ]
    return lst


def multi_rand(start, end, quantity):
    lst = []

    def gen_numbers(count, lst):
        if count > 0:
            lst2 = lst + [(randint(start, end))]
            return gen_numbers(count - 1, lst2)
        else:
            return lst
    return gen_numbers(quantity, lst)


def gen_name():
    syl_list = syllables()
    num_list = multi_rand(0, (len(syl_list) - 1), 6)
    first_name = '{}{}{}'.format(
            syl_list[num_list[0]],
            syl_list[num_list[1]],
            syl_list[num_list[2]])
    last_name = '{}{}{}'.format(
            syl_list[num_list[3]],
            syl_list[num_list[4]],
            syl_list[num_list[5]])
    name = '{} {}'.format(last_name.title(), first_name.title())

    return name


def gen_age():
    age = randint(16, 116)
    return age


def gen_phone():
    num_list = multi_rand(0, 9, 10)
    if num_list[0] != 0 and num_list[3] != 0 and num_list[0] != 1:
        phone = ''.join(map(lambda x: str(x), num_list))
        return phone
    else:
        return gen_phone()


def gen_email(name):
    name_list = name.lower().split()
    prov_list = email_providers()
    num = randint(0, (len(prov_list) - 1))
    provider = prov_list[num]
    email = '{}.{}@{}'.format(name_list[0], name_list[1], provider)
    return email


def gen_new_user():
    name = gen_name()
    last_name = name.split()[0]
    first_name = name.split()[1]
    age = gen_age()
    phone = gen_phone()
    email = gen_email(name)
    new_user = {
            'last_name': last_name, 'first_name': first_name,
            'age': age, 'phone': phone, 'email': email
            }
    return new_user
