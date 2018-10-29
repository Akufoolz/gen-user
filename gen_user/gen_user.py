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


def build_name():
    name = 'firstname lastname'
    return name
