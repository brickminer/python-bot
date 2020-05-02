from babel.numbers import format_decimal

NOT_AVAILABLE = "N/A"


def format_text(value):
    if value is None:
        return NOT_AVAILABLE

    return value


def format_currency(value):
    if value is None:
        return NOT_AVAILABLE

    return format_decimal(value, locale='en_US')
