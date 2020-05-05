from babel import numbers
import decimal

NOT_AVAILABLE: str = "N/A"
USD = "USD"
EUR = "EUR"
GBP = "GBP"
LOCALE = "en_US"


def format(value: str, code: str = USD) -> str:
    if value is None or decimal.Decimal(value) == 0.0:
        return NOT_AVAILABLE

    return numbers.format_currency(decimal.Decimal(value), code, locale=LOCALE)
