#!/usr/bin/env python3

"""
filtered_logger module

This module provides functions and classes related
 to logging and database connections.
"""
import logging
import os
import mysql.connector


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to the database """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=username, password=password, host=host, database=db_name)
