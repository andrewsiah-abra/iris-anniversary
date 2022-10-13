
import pandas as pd
import streamlit as st
import datetime as dt
from datetime import datetime, date, time, timezone


st.set_page_config(
    page_title="Iris-Andrew Anniversary", 
    page_icon="🥰",
    layout="wide",
    initial_sidebar_state="collapsed")

st.title("Iris-Andrew Anniversaries")

date_we_kissed = date(2022, 9, 14)
time_we_kissed = time(2, 00)
dt_we_kissed = dt.datetime.combine(date_we_kissed, time_we_kissed)
dt_im_bf = dt.datetime.combine(date(2022, 10, 13), time(7, 00))
dt_now = datetime.now()

st.header(f"Date We Kissed 💏: ")
st.subheader(dt_we_kissed)
st.header(f"Days Since Kissed 💋: ")
st.subheader((dt_now - dt_we_kissed).days)

st.header(f"Date I'm your BF 🥰: ")
st.subheader(dt_im_bf)
st.header(f"Days since Andrew is boyfriend 💝: ")
st.subheader((dt_now - dt_im_bf).days)

