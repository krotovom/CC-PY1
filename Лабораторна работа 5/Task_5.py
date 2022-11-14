def random_password(x=8):
    import string
    random_ = list(string.ascii_letters)
    random_.extend(string.digits)
    from random import sample
    random_pass = "".join(sample(random_, x))
    return random_pass


print(random_password())
