NOT_AVAILABLE: str = "N/A"


def format(value: str) -> str:
    if value is None:
        return NOT_AVAILABLE

    return value
