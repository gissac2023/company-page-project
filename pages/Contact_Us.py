import streamlit as st
from send_email import send_email
import pandas as pd

st.header("Contact Us")
df = pd.read_csv("topics.csv")

with st.form(key="contactform"):
    from_email = st.text_input("You Email Address")
    option = st.selectbox("What topic do you want to discuss?",
                          df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: {option} from {from_email}
From: {from_email}
Please contact in 24 hours!
\n
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Email arrived to us!")
