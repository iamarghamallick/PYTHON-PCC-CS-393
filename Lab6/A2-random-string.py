# A2. Write a function to generate a random alphanumeric string with 6 characters. There must be one uppercase, one lower case, one digit in the string and all string should start with an uppercase letter.
# Call the function 100 times and check how many time a digit is available at second position.

import random
import string

def random_str():
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    chars = string.ascii_letters + string.digits

    remaining = ''.join(random.choice(chars) for _ in range(3))

    str = upper + lower + digit + remaining

    str_list = list(str)
    random.shuffle(str_list)
    return ''.join(str_list)

count_digits = 0
for _ in range(100):
    random_string = random_str()
    if random_string[1].isdigit():
        count_digits = count_digits+1

print(count_digits)
