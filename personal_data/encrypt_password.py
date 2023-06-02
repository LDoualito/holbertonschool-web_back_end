#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted and hashed password as a byte string.

    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates if a password matches a hashed password using bcrypt.

    Args:
        hashed_password (bytes): The hashed password as a byte string.
        password (str): The password to check.

    Returns:
        bool: True if the password matches the hashed password, 
        False otherwise.

    """
    return bcrypt.checkpw(password.encode(), hashed_password)
