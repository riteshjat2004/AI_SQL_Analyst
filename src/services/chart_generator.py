import pandas as pd
import plotly.express as px
from pandas.api.types import (
    is_datetime64_any_dtype,
    is_numeric_dtype,
)


def generate_chart(df: pd.DataFrame):
    """
    Automatically selects the best Plotly chart
    based on the DataFrame structure.

    Returns:
        Plotly Figure or None
    """

    if df.empty:
        return None

    columns = df.columns.tolist()

    if len(columns) < 2:
        return None

    x = columns[0]
    y = columns[1]

    # ------------------------------------------------
    # Line Chart
    # ------------------------------------------------

    if (
        is_datetime64_any_dtype(df[x])
        or any(
            keyword in x.lower()
            for keyword in ["date", "day", "month", "year"]
        )
    ) and is_numeric_dtype(df[y]):

        return px.line(
            df,
            x=x,
            y=y,
            markers=True,
            title=f"{y} over {x}",
        )

    # ------------------------------------------------
    # Bar / Pie
    # ------------------------------------------------

    if (
        not is_numeric_dtype(df[x])
        and is_numeric_dtype(df[y])
    ):

        unique_values = df[x].nunique()

        if unique_values <= 8:

            return px.pie(
                df,
                names=x,
                values=y,
                title=f"{y} by {x}",
            )

        return px.bar(
            df,
            x=x,
            y=y,
            title=f"{y} by {x}",
        )

    # ------------------------------------------------
    # Scatter
    # ------------------------------------------------

    if (
        is_numeric_dtype(df[x])
        and is_numeric_dtype(df[y])
    ):

        return px.scatter(
            df,
            x=x,
            y=y,
            title=f"{y} vs {x}",
        )

    # ------------------------------------------------
    # Histogram
    # ------------------------------------------------

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) == 1:

        return px.histogram(
            df,
            x=numeric_columns[0],
            title=f"Distribution of {numeric_columns[0]}",
        )

    return None