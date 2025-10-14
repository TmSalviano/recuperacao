import random
import string

def password_generate(length = 12, use_uppercase = True, use_digits = True, use_special = True):
    """
        generate passwords of any strength
        Args:
            length (int): length of the password
            use_uppercase (bool): include uppercase characters
            use_digits (bool): include digits
            use_special (bool): include special characters
        Returns:
            str: password
    """

    characters = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_characters = characters + uppercase + digits + special

    password = []

    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    remainining_length = length - len(password)
    for i in range(0, remainining_length):
        password.append(random.choice(all_characters))
    
    return ''.join(password)

print(password_generate())