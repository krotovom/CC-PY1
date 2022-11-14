def get_unique_list_numbers(x1=-10, x2=10, n=15):
    import random
    list_ = []
    while len(list_) < n:
        random_int = random.randint(x1, x2)
        list_.append(random_int)
        list_ = list(set(list_))
    return list_


print(get_unique_list_numbers())
