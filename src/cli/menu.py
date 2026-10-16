class Menu:
    """
    Displays the application's terminal menu and
    collects user input.

    This class acts as the user interface for the
    Open Library Catalog System.
    """

    def display(self):
        """
        Displays the main application menu.

        The menu provides users with the available
        actions they can perform within the system.
        """

        # Print menu header
        print("\n" + "=" * 60)
        print("OPEN LIBRARY INTELLIGENCE & CATALOG SYSTEM")
        print("=" * 60)

        # Display available menu options
       # Display available menu options
        print("1. Ingest Books")
        print("2. Search Books")
        print("3. Generate Report")
        print("4. Run Tests")
        print("5. Run Ruff Check")
        print("6. Async Search")
        print("0. Exit")

        # Print menu footer
        print("=" * 60)

    def get_choice(self):
        """
        Prompts the user to select a menu option.

        Returns:
            str: The option entered by the user.
        """

        # Capture the user's menu selection
        return input("Select an option: ")