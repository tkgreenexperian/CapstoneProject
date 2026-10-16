from src.api.sync_client import SyncLibraryClient
from src.cli.menu import Menu
from src.db.library_db import LibraryDatabase
from src.processing.data_cleaner import DataCleaner
from src.reporting.book_report import BookReport
import subprocess
import asyncio

from src.api.async_client import AsyncLibraryClient


# Create objects that provide the application's functionality
client = SyncLibraryClient()
async_client = AsyncLibraryClient()
db = LibraryDatabase()
cleaner = DataCleaner()
report = BookReport()
menu = Menu()

# Create the books table if it does not already exist
db.create_table()

# Keep displaying the menu until the user chooses Exit
while True:

    # Show available menu options
    menu.display()

    # Capture the user's choice
    choice = menu.get_choice()

   # Option 1: Retrieve books from Open Library
    if choice == "1":

        # Ask the user what books they want to ingest
        search_term = input(
            "Enter topic to ingest: "
        )

        # Clean the input before sending it to the API
        search_term = cleaner.clean_title(
            search_term
        )

        # Check whether the data already exists in cache
        results = db.get_cache(
            search_term
        )

        if results is not None:

            print(
                "Using cached Open Library data."
            )

        else:

            print(
                "No valid cache found. Calling Open Library."
            )

            results = client.search_books(
                search_term
            )

            # Save API response in cache
            db.save_cache(
                search_term,
                results
            )

        # Process the first 10 returned books
        for book in results["docs"][:10]:

            # Clean title data before storing
            title = cleaner.clean_title(
                book.get("title", "Unknown")
            )

            # Retrieve author information
            authors = book.get(
                "author_name",
                ["Unknown"]
            )

            # Convert author list into a text string
            author = cleaner.clean_author(
                ", ".join(authors)
            )

            # Clean publication year data
            year = cleaner.clean_year(
                book.get("first_publish_year")
            )

            # Store cleaned data in the database
            db.save_book(
                title,
                author,
                year
            )

        print("Books loaded successfully!")

    # Option 2: Search for books already stored
    elif choice == "2":

        # Ask user which title to search for
        search_title = input(
            "Enter title to search: "
        )

        # Search local SQLite database
        books = db.search_books(search_title)

        # Display matching books
        for book in books:
            print(book)

    # Option 3: Generate reports
    elif choice == "3":

        # Retrieve all books from the database
        books = db.get_books()

        # Display analytics in the terminal
        report.generate_report(books)

        # Export report to CSV
        report.export_csv(books)

        # Export report to Excel
        report.export_excel(books)

        print("Reports generated!")

    # Option 4: Run tests
    elif choice == "4":

        print("\nRunning Tests...\n")

        subprocess.run(
            ["uv", "run", "pytest"]
        )

    # Option 5: Run Ruff check
    elif choice == "5":

        print("\nRunning Ruff Check...\n")

        subprocess.run(
            ["uv", "run", "ruff", "check", "."]
        )

    # Option 6: Async Search
    elif choice == "6":

        search_term = input(
            "Enter topic to search: "
        )

        results = asyncio.run(
            async_client.search_books(
                search_term
            )
        )

        print(
            f"\nFound {len(results['docs'])} books."
        )

    # Option 0: Exit application
    elif choice == "0":

        print("Goodbye!")
        break

    # Handle invalid menu selections
    else:

        print("Invalid option. Try again.")