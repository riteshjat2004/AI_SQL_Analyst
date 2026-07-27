from ollama import Client

from config.settings import settings


client = Client(host=settings.OLLAMA_HOST)


def generate_insights(question: str, sql: str, dataframe) -> str:
    """
    Generates business insights from the SQL result.
    """

    preview = dataframe.head(10).to_markdown(index=False)

    prompt = f"""
You are an experienced Business Data Analyst.

The user asked:

{question}

Generated SQL:

{sql}

Query Result:

{preview}

Provide:

1. A concise business summary.
2. Key observations.
3. Important trends if visible.

Keep the response under 150 words.
Do not mention SQL.
"""

    response = client.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()