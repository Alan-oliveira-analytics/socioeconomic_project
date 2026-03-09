import streamlit as st
from queries import get_indicators

# ======= PAGE CONFIG =========
st.set_page_config(
    page_title="LATAM Socioeconomic Indicators",
    layout="wide"
)

st.title("Latin America Socioeconomic Indicators")


df = get_indicators()


# ======= METRIC OVER TIME =========

options = list(df["country_id"].unique())

selection = st.segmented_control(
    "Country", 
    options, 
    selection_mode="multi",
    default=[options[0]]
)

if not selection:
    selection = [options[0]]

if selection:
    df_filter = df[df["country_id"].isin(selection)]
else:
    df_filter = df


metrics = {
    "GDP per capita": "gdp_per_capita",
    "Education expenditure": "public_education_expenditure",
    "Health expenditure": "public_health_expenditure"
}

col_chart, col_control = st.columns([4,1])

with col_control:

        metric_name = st.radio(
            "Metric",
            list(metrics.keys())
        )

y_option = metrics[metric_name]

with col_chart:
    st.subheader(f"{metric_name} over time")

    st.line_chart(
        df_filter,
        x="year",
        y=y_option,
        color="country_id"
    )


# ======= CORRELATION GRAPHICS =========

col1, col2 = st.columns(2)

with col1:
    st.text("Is there a correlation between education and GDP?")
    st.scatter_chart(
        df,
        x="public_education_expenditure",
        y="gdp_per_capita",
        y_label="GDP",
        x_label="Education Spending"
    )

with col2:
    st.text("Is there a correlation between health spending and GDP?")
    st.scatter_chart(
        df,
        x="public_health_expenditure",
        y="gdp_per_capita",
        y_label="GDP",
        x_label="Health Spending"
    )