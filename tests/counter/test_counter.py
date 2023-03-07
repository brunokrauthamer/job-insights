from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


def test_counter():
    with patch("builtins.open", mock_open(read_data="caio ABC bruno abc abc")):
        result = count_ocurrences("any path", "aBC")
        assert result == 3
