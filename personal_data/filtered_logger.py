#!/usr/bin/env python3

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class.

    This class extends the logging.Formatter class and provides a redacting formatter
    for log records. It allows filtering values in log records based on specified fields.

    Attributes:
        REDACTION (str): The string used for redacting field values.
        FORMAT (str): The log message format.
        SEPARATOR (str): The character used to separate fields in the log message.

    Args:
        fields (List[str]): The list of fields to be filtered in log records.

    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with redacted field values.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message with redacted field values.

        """
        record.msg = self.filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)

    @staticmethod
    def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        """Filter field values in the log message and replace them with the redaction string.

        Args:
            fields (List[str]): The list of fields to be filtered.
            redaction (str): The string used to replace the field values.
            message (str): The log message.
            separator (str): The character used to separate fields in the log message.

        Returns:
            str: The log message with filtered field values.

        """
        pattern = fr'({"|".join(map(re.escape, fields))})=[^{re.escape(separator)}]+(?={re.escape(separator)}|\Z)'
        return re.sub(pattern, fr'\1={redaction}', message)
