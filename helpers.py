import random, string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string