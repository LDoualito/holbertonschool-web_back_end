#!/usr/bin/env python3

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String used for obfuscation.
        message (str): Log message.
        separator (str): Character separating fields in the log message.

    Returns:
        str: Obfuscated log message.
    """
    return re.sub(fr'(?<=^|{re.escape(separator)})({"|".join(map(re.escape, fields))})=[^{re.escape(separator)}]*', fr'\1={redaction}', message)
