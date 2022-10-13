
import pandas as pd
import streamlit as st
import datetime as dt
from datetime import datetime, date, time, timezone


st.set_page_config(
    page_title="Iris-Andrew Anniversary", 
    page_icon="🥰",
    layout="wide",
    initial_sidebar_state="collapsed")

st.title("How Many Days since...")

date_we_kissed = date(2022, 9, 14)
time_we_kissed = time(2, 00)
dt_we_kissed = dt.datetime.combine(date_we_kissed, time_we_kissed)

st.write(dt_we_kissed)



