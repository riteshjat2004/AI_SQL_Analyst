from ai.prompt_builder import build_prompt

question = "Show the top 5 customers by total spending."

prompt = build_prompt(question)

print(prompt)