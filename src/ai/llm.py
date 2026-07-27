import re

from ollama import Client

from ai.prompt_builder import build_prompt
from config.settings import settings


client = Client(host=settings.OLLAMA_HOST)


def generate_sql(user_query: str) -> str:
    """
    Generates SQL from a natural language query using Ollama.
    """

    prompt = build_prompt(user_query)

    response = client.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(response) 

    sql = response["message"]["content"].strip()

    # Remove Markdown code fences if present
    sql = re.sub(r"```sql\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    return sql.strip()