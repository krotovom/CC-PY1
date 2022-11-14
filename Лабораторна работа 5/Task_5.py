import string
from random import sample


def random_password(password_length=8):
    random_ = list(string.ascii_letters)
    random_.extend(string.digits)
    random_pass = "".join(sample(random_, password_length))
    return random_pass


print(random_password())
