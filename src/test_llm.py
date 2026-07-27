from ai.prompt_builder import build_prompt
from ai.llm import generate_sql

question = "Show all customers."

prompt = build_prompt(question)

print("=" * 60)
print("PROMPT")
print("=" * 60)
print(prompt)

print("\n")

print("=" * 60)
print("GENERATED SQL")
print("=" * 60)

sql = generate_sql(question)   # <-- Pass the question, not the prompt

print(sql)