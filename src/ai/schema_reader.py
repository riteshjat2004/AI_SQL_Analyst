from sqlalchemy import inspect

from database.connection import engine


def get_database_schema() -> str:
    """
    Reads the PostgreSQL database schema and returns
    a formatted string for the LLM prompt.
    """

    inspector = inspect(engine)

    schema = []

    schema.append("Database Schema:\n")

    # Read all tables
    for table in inspector.get_table_names():

        schema.append(f"Table: {table}")

        # Read columns
        columns = inspector.get_columns(table)

        for column in columns:
            schema.append(
                f"- {column['name']} ({column['type']})"
            )

        # Read Primary Key
        pk = inspector.get_pk_constraint(table)

        if pk["constrained_columns"]:
            schema.append(
                f"Primary Key: {', '.join(pk['constrained_columns'])}"
            )

        schema.append("")

    # Read Foreign Keys
    schema.append("Relationships:")

    for table in inspector.get_table_names():

        foreign_keys = inspector.get_foreign_keys(table)

        for fk in foreign_keys:

            local_column = fk["constrained_columns"][0]
            referred_table = fk["referred_table"]
            referred_column = fk["referred_columns"][0]

            schema.append(
                f"- {table}.{local_column} -> {referred_table}.{referred_column}"
            )

    return "\n".join(schema)