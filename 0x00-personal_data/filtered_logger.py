#!/usr/bin/env python3
"""
Return the log message obfuscate
"""

import re


def filter_datum(fields, redaction, message, separator):
    """Return the log message obfuscate"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
