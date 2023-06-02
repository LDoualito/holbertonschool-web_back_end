#!/usr/bin/env python3

"""
filtered_logger module
"""

import logging
import re
from typing import Tuple

PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    def __init__(self, fields: Tuple[str, ...]):
        super().__init__("[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s")
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating sensitive information in specified fields.
        """
        return filter_datum(self.fields, '***', super().format(record), ';')


def filter_datum(fields: Tuple[str, ...], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in the log message.
    """
    for field in fields:
        pattern = fr'(?<=^|{re.escape(separator)})({"|".join(map(re.escape, [field]))})=[^{re.escape(separator)}]*'
        message = re.sub(pattern, fr'\1={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """
    Get a Logger object named "user_data".
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
