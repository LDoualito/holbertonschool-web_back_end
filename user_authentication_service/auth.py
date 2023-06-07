#!/usr/bin/env python3
""" Auth module """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ return salted hash of the input password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
