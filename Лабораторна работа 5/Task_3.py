def get_unique_list_numbers() -> list[int]:
    import random
    list_ = []
    while len(list_) <= 14:
        random_int = random.randint(-10, 10)
        list_.append(random_int)
        list_ = list(set(list_))
    return list_


print(get_unique_list_numbers())
