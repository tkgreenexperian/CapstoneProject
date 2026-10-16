import re


class DataCleaner:
    """
    Responsible for cleaning and validating data
    before it is stored in the database.
    """

    def clean_title(self, title):
        """
        Removes extra spaces from book titles.
        """

        return str(title).strip()

    def clean_author(self, author):
        """
        Removes extra spaces from author names.
        """

        return str(author).strip()

    def clean_year(self, year):
        """
        Replaces missing publication years with 0.
        """

        if year is None:
            return 0

        return year

    def extract_isbn(self, text):
        """
        Extracts an ISBN from a string using regex.
        """

        match = re.search(
            r"(97[89]\d{10}|\d{10})",
            str(text)
        )

        if match:
            return match.group()

        return None

    def validate_isbn(self, isbn):
        """
        Performs a simple ISBN format validation.

        ISBN-10 = 10 digits
        ISBN-13 = 13 digits
        """

        if isbn is None:
            return False

        isbn = isbn.replace("-", "")

        if len(isbn) == 10:
            return True

        if len(isbn) == 13:
            return True

        return False