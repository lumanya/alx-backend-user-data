"""
Encrypts the password using bcrypt
and checks if the password is valid
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts the password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the password is valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
