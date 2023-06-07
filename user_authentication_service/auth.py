#!/usr/bin/env python3
""" Auth module """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Return the salted hash of the input password.

    Args:
        password: The password to be hashed.

    Returns:
        The salted hash of the input password as bytes.
    """

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Return a string representation of a new UUID.

    Returns:
        A string representation of a new UUID.
    """

    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize a new Auth instance.
        """

        # Create a DB instance for database operations
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user in the database.

        Args:
            email: The email of the user.
            password: The password of the user.

        Returns:
            The created User object.

        Raises:
            ValueError: If the user with the provided email already exists.
        """

        try:
            # Check if the user with the provided email already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password and add the user to the database
            user = self._db.add_user(email, _hash_password(password))
            return user

    def valid_login(self, email: str, password: str) -> bool:
    """ Check if the login is valid """
    try:
        user = self._db.find_user_by(email=email)
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
    except Exception:
        return False


    def create_session(self, email: str) -> str:
        """
        Create a session for the user and return the session id.

        Args:
            email: The email of the user.

        Returns:
            The session id generated for the user.

        Raises:
            NoResultFound: If no user is found with the provided email.
        """

        try:
            # Find the user with the provided email
            user = self._db.find_user_by(email=email)

            # Generate a new session id
            session_id = _generate_uuid()

            # Update the user's session id in the database
            self._db.update_user(user.id, session_id=session_id)

            return session_id

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Get the user associated with the session id.

        Args:
            session_id: The session id of the user.

        Returns:
            The User object associated with the session id
        """

        if session_id is None:
            return None

        try:
            # Find the user with the provided session id
            user = self._db.find_user_by(session_id=session_id)
            return user

        except NoResultFound:
            return None
