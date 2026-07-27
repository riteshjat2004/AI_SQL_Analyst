import pandas as pd
import plotly.express as px


def generate_chart(df: pd.DataFrame):
    """
    Automatically generates the most suitable Plotly chart
    based on the DataFrame structure.

    Returns:
        Plotly Figure or None
    """

    if df.empty:
        return None

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    # Need at least one numeric column
    if not numeric_columns:
        return None

    # -----------------------------
    # Line Chart (Date + Numeric)
    # -----------------------------
    if len(df.columns) == 2:

        x = df.columns[0]
        y = df.columns[1]

        if "date" in x.lower():
            return px.line(df, x=x, y=y)

        if "month" in x.lower():
            return px.line(df, x=x, y=y)

        if "year" in x.lower():
            return px.line(df, x=x, y=y)

    # -----------------------------
    # Bar Chart
    # -----------------------------
    if len(categorical_columns) >= 1:

        x = categorical_columns[0]
        y = numeric_columns[0]

        return px.bar(df, x=x, y=y)

    # -----------------------------
    # Histogram
    # -----------------------------
    return px.histogram(
        df,
        x=numeric_columns[0],
    )