import json
import sqlite3
from datetime import datetime, timedelta, timezone


class LibraryDatabase:
    """
    Manages book records and cached API responses
    in the application's SQLite database.
    """

    def __init__(self):
        """
        Connects to the SQLite database and creates
        a cursor for executing SQL statements.
        """

        self.connection = sqlite3.connect(
            "data/library.db"
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        """
        Creates the books and API cache tables
        if they do not already exist.
        """

        # Stores book records retrieved from Open Library
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER
            )
            """
        )

        # Stores API responses so repeated searches
        # do not always require another API request
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS api_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT UNIQUE NOT NULL,
                response TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )

        self.connection.commit()

    def save_book(self, title, author, year):
        """
        Saves one book in the books table.

        Args:
            title (str): The book title.
            author (str): The book author or authors.
            year (int): The first publication year.
        """

        self.cursor.execute(
            """
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
            """,
            (title, author, year),
        )

        self.connection.commit()

    def get_books(self):
        """
        Retrieves all books stored in the database.

        Returns:
            list: All book records as tuples.
        """

        self.cursor.execute(
            "SELECT * FROM books"
        )

        return self.cursor.fetchall()

    def search_books(self, title):
        """
        Searches stored books using a full or partial title.

        Args:
            title (str): The title text to search for.

        Returns:
            list: Matching book records as tuples.
        """

        self.cursor.execute(
            """
            SELECT *
            FROM books
            WHERE title LIKE ?
            """,
            (f"%{title}%",),
        )

        return self.cursor.fetchall()

    def save_cache(self, query, response):
        """
        Saves an API response in the cache.

        If the query already exists, the old cached response
        and timestamp are replaced with the new values.

        Args:
            query (str): The API search term.
            response (dict): The API response to cache.
        """

        # Convert the Python dictionary into JSON text
        response_json = json.dumps(response)

        # Record when the response was cached
        created_at = datetime.now(
            timezone.utc
        ).isoformat()

        self.cursor.execute(
            """
            INSERT INTO api_cache (
                query,
                response,
                created_at
            )
            VALUES (?, ?, ?)
            ON CONFLICT(query)
            DO UPDATE SET
                response = excluded.response,
                created_at = excluded.created_at
            """,
            (
                query.lower(),
                response_json,
                created_at,
            ),
        )

        self.connection.commit()

    def get_cache(self, query, expiration_minutes=60):
        """
        Retrieves a cached API response when it is still valid.

        A cached response older than the expiration period is
        deleted and treated as missing.

        Args:
            query (str): The API search term.
            expiration_minutes (int): Cache lifetime in minutes.

        Returns:
            dict | None: Cached API data, or None if no valid
            cached response exists.
        """

        self.cursor.execute(
            """
            SELECT response, created_at
            FROM api_cache
            WHERE query = ?
            """,
            (query.lower(),),
        )

        cached_row = self.cursor.fetchone()

        # No cached response exists for this query
        if cached_row is None:
            return None

        response_json, created_at_text = cached_row

        created_at = datetime.fromisoformat(
            created_at_text
        )

 