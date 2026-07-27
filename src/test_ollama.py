from ai.llm import generate_sql

question = "Show the top 5 customers by total spending."

sql = generate_sql(question)

print(sql)