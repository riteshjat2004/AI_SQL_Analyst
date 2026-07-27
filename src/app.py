import streamlit as st

from src.services.query_executor import execute_query

st.set_page_config(
    page_title="AI SQL Data Analyst",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI SQL Data Analyst")

st.write(
    "Ask questions about your PostgreSQL database using natural language."
)

question = st.text_input(
    "Enter your question",
    placeholder="Example: Show top 5 products",
)

if st.button("Ask AI"):

    # Temporary SQL (LLM will generate this later)
    sql_query = """
    SELECT
        product_name,
        category,
        price
    FROM products
    LIMIT 10;
    """

    st.subheader("Generated SQL")

    st.code(sql_query, language="sql")

    df = execute_query(sql_query)
    st.subheader("Results")

    st.dataframe(df, use_container_width=True)
