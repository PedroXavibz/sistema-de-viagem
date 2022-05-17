"""
Converter strings
"""

import datetime


def convert_string_to_date(string: str) -> datetime.datetime | bool:
    """
    Converte uma string em um datetime

    Args:
        string:

    Returns:
        datetime:
    """
    string_splited: list[str] = string.split('/')
    day: int = int(string_splited[0])
    month: int = int(string_splited[1])
    year: int = int(string_splited[2])

    try:
        date = datetime.datetime(year=year, month=month, day=day)
    except ValueError:
        return False

    return date
