#!/usr/bin/env python3

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = self.filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)

    @staticmethod
    def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        pattern = fr'({"|".join(map(re.escape, fields))})=[^{re.escape(separator)}]+(?={re.escape(separator)}|\Z)'
        return re.sub(pattern, fr'\1={redaction}', message)
