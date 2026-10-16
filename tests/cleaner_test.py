"""
Unit tests for the DataCleaner class.

These tests verify that cleaning and validation
functions behave as expected.
"""

from src.processing.data_cleaner import DataCleaner


def test_clean_title():
    """
    Verify that extra spaces are removed
    from book titles.
    """

    cleaner = DataCleaner()

    result = cleaner.clean_title(
        "  Learning Python  "
    )

    assert result == "Learning Python"


def test_clean_author():
    """
    Verify that extra spaces are removed
    from author names.
    """

    cleaner = DataCleaner()

    result = cleaner.clean_author(
        "  Mark Lutz  "
    )

    assert result == "Mark Lutz"


def test_extract_isbn():
    """
    Verify that a valid ISBN can be extracted
    from a text string using regex.
    """

    cleaner = DataCleaner()

    result = cleaner.extract_isbn(
        "ISBN: 9780135166307"
    )

    assert result == "9780135166307"


def test_validate_isbn():
    """
    Verify that a valid ISBN-13 returns True.
    """

    cleaner = DataCleaner()

    assert cleaner.validate_isbn(
        "9780135166307"
    ) is True


def test_invalid_isbn():
    """
    Verify that an invalid ISBN returns False.
    """

    cleaner = DataCleaner()

    assert cleaner.validate_isbn(
        "12345"
    ) is False