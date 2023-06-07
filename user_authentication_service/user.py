#!/usr/bin/env python3

"""Create an SQLAlchemy model"""

# Import necessary modules
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base class for declarative models
Base = declarative_base()


# Define a class representing the User model
class User(Base):
    """
    User model representing the users table in the database.
    """

    # Specify the table name
    __tablename__ = 'users'

    # Define columns for the User model
    id = Column(Integer, primary_key=True)
    """
    id: Integer column
        Primary key column for identifying the user.
    """

    email = Column(String(250), nullable=False)
    """
    email: String column
        Column to store the email of the user.
        The maximum length is set to 250 characters.
        The email cannot be nullable (required).
    """

    hashed_password = Column(String(250), nullable=False)
    """
    hashed_password: String column
        Column to store the hashed password of the user.
        The maximum length is set to 250 characters.
        The hashed password cannot be nullable (required).
    """

    session_id = Column(String(250), nullable=True)
    """
    session_id: String column
        Column to store the session ID of the user.
        The maximum length is set to 250 characters.
        The session ID can be nullable.
    """

    reset_token = Column(String(250), nullable=True)
    """
    reset_token: String column
        Column to store the reset token of the user.
        The maximum length is set to 250 characters.
        The reset token can be nullable.
    """
