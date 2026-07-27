from sqlalchemy import text
import pandas as pd

from database.connection import engine
from ai.llm import generate_sql
from ai.sql_validator import validate_sql


def ask_database(user_query: str) -> tuple[str, pd.DataFrame]:
    """
    Generates SQL from a natural language query,
    validates it, executes it, and returns the
    SQL along with the query result.
    """

    sql = generate_sql(user_query)

    sql = validate_sql(sql)

    with engine.connect() as connection:
        df = pd.read_sql(text(sql), connection)

    return sql, df