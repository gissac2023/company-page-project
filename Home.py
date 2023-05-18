import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")
st.info("I think i will go running later!")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv", sep=",")  # defualt is ,

with col1:
    for index, row in df[:4].iterrows():
        # st.header(row["first name"] + " " + row["last name"])
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
