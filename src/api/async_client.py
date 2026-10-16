import httpx

from src.exceptions import APIError


class AsyncLibraryClient:
    """
    Handles asynchronous communication with the Open Library API.

    Unlike the SyncLibraryClient, this class uses async/await
    so that multiple API requests can be processed concurrently.
    """

    # Base URL used for all Open Library API requests
    BASE_URL = "https://openlibrary.org"

    async def search_books(self, query):
        """
        Searches Open Library asynchronously using a search term.

        Args:
            query (str): Title, keyword, or phrase to search for.

        Returns:
            dict: JSON response converted into a Python dictionary.

        Raises:
            APIError: If the API request fails.
        """

        # Build search URL using the user's query
        url = f"{self.BASE_URL}/search.json?q={query}"

        try:

            # Create an asynchronous HTTP client
            async with httpx.AsyncClient(
                verify=False
            ) as client:

                # Send asynchronous GET request
                response = await client.get(url)

                # Raise an exception if the API call fails
                response.raise_for_status()

                # Convert JSON response into Python dictionary
                return response.json()

        except httpx.HTTPError as e:

            # Convert HTTP errors into a custom application error
            raise APIError(
                f"Unable to retrieve books: {e}"
            )

    async def search_books_by_page(
        self,
        query,
        page
    ):
        """
        Searches Open Library and retrieves a specific page
        of results.

        This supports pagination when there are more results
        than can fit on a single page.

        Args:
            query (str): Search term.
            page (int): Page number to retrieve.

        Returns:
            dict: JSON response converted into a Python dictionary.
        """

        # Build URL with query and page parameter
        url = (
            f"{self.BASE_URL}"
            f"/search.json?q={query}"
            f"&page={page}"
        )

        # Create asynchronous HTTP client
        async with httpx.AsyncClient(
            verify=False
        ) as client:

            # Request specific page of results
            response = await client.get(url)

            # Return JSON response as a Python dictionary
            return response.json()