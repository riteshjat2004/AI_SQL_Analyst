from sqlalchemy import text
import pandas as pd

from src.database.connection import engine


def execute_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns a Pandas DataFrame.
    """

    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)

    return df