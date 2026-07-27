from ai.schema_reader import get_database_schema


def build_prompt(user_query: str) -> str:
    """
    Builds a schema-aware prompt for the LLM.
    """

    schema = get_database_schema()

    prompt = f"""
You are an expert PostgreSQL SQL generator.

Database Schema:
{schema}

Rules:
1. Generate only PostgreSQL SQL.
2. Use only the tables and columns provided in the schema.
3. Do not invent table or column names.
4. Generate only SELECT queries.
5. Do not use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, or TRUNCATE.
6. Return only the SQL query without any explanation or markdown.

User Question:
{user_query}
"""

    return prompt.strip()