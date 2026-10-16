import pandas as pd


class BookReport:
    """
    Responsible for generating analytics and exporting reports.

    This class converts book data retrieved from the database
    into a pandas DataFrame and uses that data to create
    summary statistics and export files.
    """

    def generate_report(self, books):
        """
        Creates a pandas DataFrame and displays summary
        statistics about the books stored in the database.

        Args:
            books (list): List of book records retrieved
            from SQLite.
        """

        # Convert database records into a pandas DataFrame
        df = pd.DataFrame(
            books,
            columns=["id", "title", "author", "year"]
        )

        print("\nReport Summary")
        print("-" * 20)

        # Count total records in the DataFrame
        print(f"Total Books: {len(df)}")

        # Count unique author names
        print(f"Unique Authors: {df['author'].nunique()}")

        # Find earliest publication year
        print(f"Oldest Year: {df['year'].min()}")

        # Find most recent publication year
        print(f"Newest Year: {df['year'].max()}")

    def export_csv(self, books):
        """
        Exports book data to a CSV file.

        Args:
            books (list): List of book records retrieved
            from SQLite.
        """

        # Convert database records to a DataFrame
        df = pd.DataFrame(
            books,
            columns=["id", "title", "author", "year"]
        )

        # Save report as a CSV file
        df.to_csv(
            "data/books.csv",
            index=False
        )

    def export_excel(self, books):
        """
        Exports book data to an Excel workbook.

        Args:
            books (list): List of book records retrieved
            from SQLite.
        """

        # Convert database records to a DataFrame
        df = pd.DataFrame(
            books,
            columns=["id", "title", "author", "year"]
        )

        # Save report as an Excel file
        df.to_excel(
            "data/books.xlsx",
            index=False
        )