#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """
    DB class representing the database operations.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        """

        # Create a SQLAlchemy engine for database connection
        self._engine = create_engine("sqlite:///a.db")

        # Drop all existing tables and create new ones
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)

        # Initialize the session object as None
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object.
        Lazily creates and returns a session if it doesn't exist.
        """

        if self.__session is None:
            # Create a session factory and bind it to the engine
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()

        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Save a new user to the database.

        Args:
            email: Email address of the user.
            hashed_password: Hashed password of the user.

        Returns:
            The created user object.
        """

        session = self._session

        # Create a new User object with the provided email and hashed_password
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the new_user object to the session
        session.add(new_user)

        # Commit the changes to the database
        session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user in the database based on the provided criteria.

        Args:
            kwargs: Keyword arguments representing the search criteria.

        Returns:
            The found user object.

        Raises:
            NoResultFound: If no user is found with the provided criteria.
            InvalidRequestError: If an invalid request is made.
        """

        try:
            session = self._session

            # Perform a query on the User model and filter
            user = session.query(User).filter_by(**kwargs).first()

            if user is None:
                raise NoResultFound

            return user

        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user in the database.

        Args:
            user_id: The ID of the user to be updated.
            kwargs: Keyword arguments representing the fields to be updated.

        Raises:
            ValueError: If an invalid field is provided for updating.

        Returns:
            None.
        """

        valid = ['email', 'hashed_password', 'session_id', 'reset_token']

        session = self._session

        # Find the user to be updated based on the user_id
        user = self.find_user_by(id=user_id)

        # Update the user's fields based on the provided kwargs
        for key, val in kwargs.items():
            if key not in valid:
                raise ValueError
            setattr(user, key, val)

        # Commit the changes to the database
        session.commit()

        return None
