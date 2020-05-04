from babel.numbers import format_decimal

NOT_AVAILABLE: str = "N/A"


def format(value: str) -> str:
    if value is None:
        return NOT_AVAILABLE

    return format_decimal(value, locale='en_US')
