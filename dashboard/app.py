import streamlit as st
import pandas as pd
from pathlib import Path

# data visualization
import altair as alt
import plotly.express as px


# ======= PAGE CONFIG =========

st.set_page_config(
    page_title="LATAM Socioeconomic Indicators",
    layout="wide"
)

st.title("Latin America Socioeconomic Indicators")
st.text("Dataset -> https://servicodados.ibge.gov.br/api/docs/paises")

BASE_DIR = Path(__file__).resolve().parent.parent
parquet_path = BASE_DIR / "data" / "socioeconomic_data.parquet"

df = pd.read_parquet(parquet_path)

# ======= INDICATORS =========

a, b, c = st.columns(3)
a.metric(label="AVG GDP per capita", value=f"R$ {df['gdp_per_capita'].mean():,.2f}", border=True)
b.metric(label="AVG Education Spending", value=f"R$ {df['public_education_expenditure'].mean():,.2f}", border=True)
c.metric(label="AVG Health Spending", value=f"R$ {df['public_health_expenditure'].mean():,.2f}", border=True)



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
    st.text(f"{metric_name} over time")
    df_plot = (
    df_filter
    .groupby(["country_id", "year"], as_index=False)[y_option]
    .mean()
    )
    
    fig1 = px.line(
    df_plot,
    x="year",
    y=y_option,
    color="country_id",
    markers=True
)
    
    st.plotly_chart(fig1)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
st.markdown("<hr style='border: none; border-top: 1px solid rgba(107, 114, 128, 0.35); margin: 0 0 1.5rem 0;'>", unsafe_allow_html=True)

# ======= TOP 10 GRAPHS =========

year_filter = st.selectbox(
    "Select Year",
    sorted(df["year"].unique()),
    index=len(sorted(df["year"].unique())) - 1
)

df_year = df[df["year"] == year_filter]

col1, col2, col3 = st.columns(3, gap="large")

def top10_chart(df, column, label):

    top10 = (
        df
        .groupby("country_id", as_index=False)[column]
        .max()
        .sort_values(column, ascending=False)
        .head(10)
    )

    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(column, title=""),
            y=alt.Y(
                "country_id:N",
                sort="-x",
                title=""
            ),
            tooltip=["country_id", column]
        )
        .properties(
            height=300,
            title=label
        )
    )

    st.altair_chart(chart, use_container_width=True)

with col1:
    top10_chart(df_year, "gdp_per_capita", "Top 10 Countries by GDP per capita")

with col2:
    top10_chart(df_year, "public_education_expenditure", "Top 10 Countries by Education Spending")

with col3:
    top10_chart(df_year, "public_health_expenditure", "Top 10 Countries by Health Spending")


st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
st.markdown("<hr style='border: none; border-top: 1px solid rgba(107, 114, 128, 0.35); margin: 0 0 1.5rem 0;'>", unsafe_allow_html=True)

# ======= CORRELATION GRAPHICS =========

col1, col2, col3 = st.columns([1, 1, 0.4], gap="large")

corr_edu = df["public_education_expenditure"].corr(df["gdp_per_capita"])
corr_health = df["public_health_expenditure"].corr(df["gdp_per_capita"])

with col1:
    st.text("Is there a correlation between education and GDP?")
    fig = px.scatter(
        df,
        x="public_education_expenditure",
        y="gdp_per_capita",
        trendline="ols"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.text("Is there a correlation between health spending and GDP?")
    fig = px.scatter(
        df,
        x="public_health_expenditure",
        y="gdp_per_capita",
        trendline="ols"
    )

    st.plotly_chart(fig, use_container_width=True)

with col3:
    # Offset the metric cards so the pair sits centered relative to the charts.
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

    st.metric(
        label="Education vs GDP Correlation",
        value=f"{corr_edu:.2f}",
        border=True
    )

    st.metric(
        label="Health vs GDP Correlation",
        value=f"{corr_health:.2f}",
        border=True
    )

# row dataset

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
st.markdown("<hr style='border: none; border-top: 1px solid rgba(107, 114, 128, 0.35); margin: 0 0 1.5rem 0;'>", unsafe_allow_html=True)

st.text("Is there a correlation between health spending and education spending?")
fig = px.scatter(
        df,
        x="public_health_expenditure",
        y="public_education_expenditure",
        trendline="ols"
    )
st.plotly_chart(fig, use_container_width=True)