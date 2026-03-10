import streamlit as st
from queries import get_indicators

# ======= PAGE CONFIG =========

st.set_page_config(
    page_title="LATAM Socioeconomic Indicators",
    layout="wide"
)

st.title("Latin America Socioeconomic Indicators")


df = get_indicators()

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
    st.line_chart(
        df_filter,
        x="year",
        y=y_option,
        color="country_id"
    )

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
st.markdown("<hr style='border: none; border-top: 1px solid rgba(107, 114, 128, 0.35); margin: 0 0 1.5rem 0;'>", unsafe_allow_html=True)



# ======= CORRELATION GRAPHICS =========

col1, col2, col3 = st.columns([1, 1, 0.4], gap="large")

corr_edu = df["public_education_expenditure"].corr(df["gdp_per_capita"])
corr_health = df["public_health_expenditure"].corr(df["gdp_per_capita"])

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
st.scatter_chart(
        df,
        x="public_health_expenditure",
        y="public_education_expenditure",
        y_label="GDP",
        x_label="Health Spending"
    )
