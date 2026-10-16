"""
Custom exceptions used throughout the application.

These exceptions make error handling easier to understand
and help identify exactly where a problem occurred.
"""

class APIError(Exception):
    """Raised when an API request fails."""


class DataValidationError(Exception):
    """Raised when data validation fails."""


class DatabaseError(Exception):
    """Raised when database operations fail."""
