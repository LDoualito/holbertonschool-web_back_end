#!/usr/bin/env python3

import os
import mysql.connector

def get_db():
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.environ.get('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
