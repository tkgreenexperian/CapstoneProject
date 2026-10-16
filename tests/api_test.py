from src.api.sync_client import SyncLibraryClient


def test_search_books():
    client = SyncLibraryClient()
    results = client.search_books(
        "python"
    )

    assert "docs" in results