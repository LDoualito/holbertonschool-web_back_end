#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth.
    For the moment this class will be empty"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """method in the class BasicAuth that returns the Base64
        part of the Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        afterbas = authorization_header.split(" ")[1]
        return afterbas

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method in the class BasicAuth that returns the decoded
        value of a Base64 string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            b64decode = base64.b64decode(base64_authorization_header)
            utf8 = b64decode.decode('utf-8')
        except Exception:
            return
        return utf8

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        afterbas = decoded_base64_authorization_header.split(":", (1))
        return (afterbas[0], afterbas[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """class BasicAuth that returns the User
        instance based on his email and password"""
        if type(user_email) != str:
            return None
        if type(user_pwd) != str:
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return

        for i in user:
            if i.is_valid_password(user_pwd):
                return i
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves
        the User instance for a request"""
        authorization = self.authorization_header(request)

        if not authorization:
            return None

        extract_base64 = self.extract_base64_authorization_header(
            authorization)

        if not extract_base64:
            return None

        decode_base64 = self.decode_base64_authorization_header(extract_base64)

        if not decode_base64:
            return None

        email, password = self.extract_user_credentials(decode_base64)

        if not email or not password:
            return None

        user_object = self.user_object_from_credentials(email, password)

        return user_object
