import re


def validate_sql(sql: str) -> str:
    """
    Validates that the generated SQL is safe to execute.
    Only SELECT and WITH queries are allowed.
    """

    sql = sql.strip()

    if not sql:
        raise ValueError("Generated SQL is empty.")

    # Remove comments
    sql = re.sub(r"--.*", "", sql)
    sql = re.sub(r"/\*.*?\*/", "", sql, flags=re.DOTALL)

    sql_upper = sql.upper()

    # Only allow SELECT or WITH queries
    if not (
        sql_upper.startswith("SELECT")
        or sql_upper.startswith("WITH")
    ):
        raise ValueError("Only SELECT queries are allowed.")

    # Block dangerous SQL keywords
    blocked_keywords = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "GRANT",
        "REVOKE",
    ]

    for keyword in blocked_keywords:
        if re.search(rf"\b{keyword}\b", sql_upper):
            raise ValueError(f"Unsafe SQL detected: {keyword}")

    return sql