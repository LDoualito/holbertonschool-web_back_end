#!/usr/bin/env python3

import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


def get_db() -> MySQLConnection:
    username: str = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password: str = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host: str = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    database: str = os.environ.get('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
