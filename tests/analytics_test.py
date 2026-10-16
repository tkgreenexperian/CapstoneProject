import pandas as pd


def test_dataframe_creation():
    data = [
        (
            1,
            "Learning Python",
            "Mark Lutz",
            1999
        )
    ]

    df = pd.DataFrame(
        data,
        columns=[
            "id",
            "title",
            "author",
            "year"
        ]
    )

    assert len(df) == 1
