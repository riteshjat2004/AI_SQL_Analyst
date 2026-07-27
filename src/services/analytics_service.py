import time

from ai.insight_generator import generate_insights
from services.query_executor import ask_database
from utils.chart_generator import generate_chart


def analyze_question(question: str) -> dict:
    """
    Executes the complete AI analytics pipeline.
    """

    start_time = time.perf_counter()

    sql, dataframe = ask_database(question)

    execution_time = time.perf_counter() - start_time

    chart = generate_chart(dataframe)

    insight = generate_insights(
        question,
        sql,
        dataframe,
    )

    return {
        "sql": sql,
        "dataframe": dataframe,
        "chart": chart,
        "insight": insight,
        "execution_time": execution_time,
        "rows": len(dataframe),
    }