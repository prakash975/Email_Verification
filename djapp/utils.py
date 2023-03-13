import random
import string

def generate_random_code(length=6):
    """Generate a random code of the specified length"""
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
