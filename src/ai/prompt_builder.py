from ai.schema_reader import get_database_schema


def build_prompt(user_query: str) -> str:
    """
    Builds a schema-aware prompt for SQL generation.
    """

    schema = get_database_schema()

    prompt = f"""
You are an expert PostgreSQL Data Analyst.

Database Schema:

{schema}

Your task is to generate accurate PostgreSQL SQL queries.

Rules:

1. Use ONLY the tables and columns provided.
2. Never invent table names.
3. Never invent column names.
4. Generate ONLY executable PostgreSQL SQL.
5. Return ONLY SQL.
6. Never use markdown.
7. Never explain the query.
8. Never generate INSERT.
9. Never generate UPDATE.
10. Never generate DELETE.
11. Never generate DROP.
12. Never generate ALTER.
13. Never generate CREATE.
14. Prefer explicit column names instead of SELECT *.
15. Use meaningful aliases.
16. Use JOINs only when required.
17. Use GROUP BY correctly.
18. Use ORDER BY whenever ranking is requested.
19. Use LIMIT for Top/Bottom queries.
20. Optimize the query for readability.

User Question:

{user_query}
"""

    return prompt