from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

def login_screen():
    st.subheader("This app is private.")
    st.write("Please log in to proceed ...")
    st.button("Sign in with Microsoft", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.write(f"Welcome to Parexel: {st.user.name}!")
    st.caption("User details")
    st.user
    if st.button("Sign out"):
        st.logout()
