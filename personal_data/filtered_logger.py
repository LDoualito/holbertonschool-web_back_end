#!/usr/bin/env python3

import logging
from typing import List

PII_FIELDS: List[str] = ['name', 'email', 'phone', 'ssn', 'password']

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    def __init__(self, fields: List[str]):
        super().__init__("[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s")
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, '***', super().format(record), ';')


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Returns the log message obfuscated """

    for field in fields:
        message = re.sub(fr'(?<=^|{re.escape(separator)})({"|".join(map(re.escape, [field]))})=[^{re.escape(separator)}]*', fr'\1={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """ Returns a Logger object named "user_data" """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
