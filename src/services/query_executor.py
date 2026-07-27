from sqlalchemy import text
import pandas as pd

from ai.llm import generate_sql
from ai.sql_validator import validate_sql
from database.connection import engine


def ask_database(user_query: str) -> tuple[str, pd.DataFrame]:
    """
    Converts a natural language question into SQL,
    validates it, executes it, and returns the result.
    """

    sql = generate_sql(user_query)
    sql = validate_sql(sql)

    with engine.connect() as connection:
        dataframe = pd.read_sql(text(sql), connection)

    return sql, dataframe