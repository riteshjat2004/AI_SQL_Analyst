import streamlit as st

from services.query_executor import ask_database

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
    placeholder="Example: Show top 5 products by revenue",
)

if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:
        sql, df = ask_database(question)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        st.subheader("Results")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(str(e))