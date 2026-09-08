from unittest.mock import Mock

from mya.assistant import Assistant


def test_reports_name():
    result = Assistant().handle("What is your name?")
    assert "MYA" in result.reply


def test_exit_command():
    result = Assistant().handle("goodbye")
    assert result.should_exit is True


def test_search_encodes_query():
    opener = Mock()
    result = Assistant(opener=opener).handle("search for python voice recognition")
    opener.assert_called_once_with("https://www.google.com/search?q=python+voice+recognition")
    assert result.should_exit is False


def test_unknown_command_is_safe():
    result = Assistant().handle("launch the moon")
    assert "don't know" in result.reply
