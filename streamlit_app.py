from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.user
    st.header(f"Welcome, {st.user.name}!")

