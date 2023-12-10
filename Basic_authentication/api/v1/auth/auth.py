#!/usr/bin/env python3
"""create a class to manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Vlass"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth"""
        if path is None or excluded_paths is None:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header"""
        if request is None and "Authorization" not in request.headers:
            return None
        auth = request.headers.get("Authorization")
        if (auth):
            return (auth)
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user"""
        return None
