"""
Encrypts the password using bcrypt
"""
import bcrypt


def hash_password(password):
    """Encrypts the password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
