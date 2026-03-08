import streamlit as st
from queries import get_indicators

st.title("Latin America Socioeconomic Indicators")

df = get_indicators()

st.dataframe(df)