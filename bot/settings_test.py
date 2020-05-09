from .settings import Settings
from mock import patch


@patch("os.environ.get", return_value="conn_string")
def test_db_connection(mock):
    settings = Settings()
    dc = settings.db_connection()

    mock.assert_called_once_with("DB_CONNECTION")
    assert dc == "conn_string"


@patch("os.environ.get", return_value="token")
def test_telegram_token(mock):
    settings = Settings()
    tt = settings.telegram_token()

    mock.assert_called_once_with("TELEGRAM_TOKEN")
    assert tt == "token"


@patch("os.environ.get", return_value="on")
def test_debug_queries_is_on(mock):
    settings = Settings()
    dq = settings.debug_queries()

    mock.assert_called_once_with("DEBUG_QUERIES")
    assert dq == True


@patch("os.environ.get", return_value="")
def test_debug_queries_is_off(mock):
    settings = Settings()
    dq = settings.debug_queries()

    mock.assert_called_once_with("DEBUG_QUERIES")
    assert dq == False


@patch("os.environ.get", return_value="1111,2222")
def test_with_blocked_sets(mock):
    settings = Settings()
    bs = settings.blocked_sets()

    mock.assert_called_with("BLOCKED_SETS")
    assert mock.call_count == 2
    assert bs == ["1111", "2222"]


@patch("os.environ.get", return_value="")
def test_without_blocked_sets(mock):
    settings = Settings()
    bs = settings.blocked_sets()

    mock.assert_called_with("BLOCKED_SETS")
    assert mock.call_count == 1
    assert bs == []
