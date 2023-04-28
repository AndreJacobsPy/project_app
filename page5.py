import streamlit as st
from page2 import filterer


def user_comparisons(data):
    # get user input
    num = st.number_input("How many subsets?", step=1, min_value=1)

    for i in range(num):
        df = filterer(data)
        st.table(df)
