#!/usr/bin/env python3

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

def main() -> None:
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter('[HOLBERTON] user_data INFO %(asctime)s: name=***; email=***; phone=***; ssn=***; password=***; ip=%(ip)s; last_login=%(last_login)s; user_agent=%(user_agent)s;')
    redacting_formatter = logging.Formatter('[HOLBERTON] user_data INFO %(asctime)s: name=***; email=***; phone=***; ssn=***; password=***; ip=%(ip)s; last_login=%(last_login)s; user_agent=%(user_agent)s;\nFiltered fields:\n\nname\nemail\nphone\nssn\npassword')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(redacting_formatter)

    logger.addHandler(stream_handler)

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        record = {
            'name': row[0],
            'email': row[1],
            'phone': row[2],
            'ssn': row[3],
            'password': row[4],
            'ip': row[5],
            'last_login': row[6].strftime('%Y-%m-%d %H:%M:%S'),
            'user_agent': row[7]
        }
        logger.info('', extra=record)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
