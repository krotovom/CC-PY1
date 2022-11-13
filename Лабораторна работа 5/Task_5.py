def random_password():
    import string
    random_ = list(string.ascii_letters)
    random_.extend(string.digits)
    from random import sample
    random_pass = "".join(sample(random_, 8))
    return random_pass


print(random_password())