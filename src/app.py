import time

import streamlit as st

from ai.insight_generator import generate_insights
from services.query_executor import ask_database
from utils.chart_generator import generate_chart

st.set_page_config(
    page_title="AI SQL Data Analyst",
    page_icon="🤖",
    layout="wide",
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI SQL Data Analyst")

st.write(
    "Ask questions about your PostgreSQL database using natural language."
)

question = st.text_input(
    "Enter your question",
    placeholder="Example: Show top 5 products by revenue",
)

# --------------------------------------------------
# Ask AI
# --------------------------------------------------

if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:

        with st.spinner("Generating SQL and querying database..."):

            start_time = time.perf_counter()

            sql, df = ask_database(question)

            execution_time = time.perf_counter() - start_time

        # Save history
        st.session_state.history.append(question)

        # ------------------------------------------
        # SQL
        # ------------------------------------------

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # ------------------------------------------
        # Metrics
        # ------------------------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Execution Time",
                f"{execution_time:.2f} sec",
            )

        with col2:
            st.metric(
                "Rows Returned",
                len(df),
            )

        # ------------------------------------------
        # Results
        # ------------------------------------------

        st.subheader("Results")

        st.dataframe(
            df,
            use_container_width=True,
        )

        # ------------------------------------------
        # Download CSV
        # ------------------------------------------

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="query_results.csv",
            mime="text/csv",
        )

        # ------------------------------------------
        # Visualization
        # ------------------------------------------

        fig = generate_chart(df)

        if fig is not None:

            st.subheader("Visualization")

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        # ------------------------------------------
        # AI Business Insight
        # ------------------------------------------

        with st.spinner("Generating AI insights..."):

            insight = generate_insights(
                question,
                sql,
                df,
            )

        st.subheader("AI Business Insight")

        st.write(insight)

    except Exception as e:
        st.error(f"❌ {e}")

# --------------------------------------------------
# Query History
# --------------------------------------------------

if st.session_state.history:

    st.divider()

    col1, col2 = st.columns([4, 1])

    with col1:
        st.subheader("Query History")

    with col2:
        if st.button("🗑 Clear History"):
            st.session_state.history = []
            st.rerun()

    for index, item in enumerate(
        reversed(st.session_state.history),
        start=1,
    ):
        st.write(f"{index}. {item}")