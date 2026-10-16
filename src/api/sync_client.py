import httpx


class SyncLibraryClient:
    """
    Handles synchronous communication with the Open Library API.

    This class is responsible for sending requests to Open Library
    and returning book data to the rest of the application.
    """

    # Base URL used for all Open Library API requests
    BASE_URL = "https://openlibrary.org"

    def search_books(self, query):
        """
        Searches Open Library for books matching a title,
        keyword, author, or phrase entered by the user.

        Args:
            query (str): Search term entered by the user.

        Returns:
            dict: JSON response converted into a Python dictionary.
        """

        # Build the complete API endpoint URL
        url = f"{self.BASE_URL}/search.json?q={query}"

        # Send an HTTP GET request to Open Library
        response = httpx.get(url, verify=False)

        # Convert JSON response into a Python dictionary
        return response.json()