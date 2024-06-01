import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
_,header,_ = st.columns([1,2,1])
header.markdown("## Playstore ratings analysis")
ratings = pd.read_csv("./ratings.csv")
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(data=ratings, x='Genre', y='Rating', use_container_width=True)
    st.line_chart(data=ratings, x='Developer', y='Rating', use_container_width=True)

with col2:
    st.area_chart(data=ratings, x='Developer', y='Rating', use_container_width=True)
    st.scatter_chart(data=ratings, x='Genre', y='Rating', use_container_width=True)