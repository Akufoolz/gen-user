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
    age = 0
    return age
