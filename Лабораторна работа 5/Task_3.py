import random


def get_unique_list_numbers(left_edge=-10, right_edge=10, list_length=15):
    list_ = []
    while len(list_) < list_length:
        random_int = random.randint(left_edge, right_edge)
        list_.append(random_int)
        list_ = list(set(list_))
    return list_


print(get_unique_list_numbers())
