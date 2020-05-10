NOT_AVAILABLE: str = "N/A"


def format(value: str) -> str:
    if value is None or value == "":
        return NOT_AVAILABLE

    return value
