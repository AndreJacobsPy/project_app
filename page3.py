import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use("dark_background")


def stats_table(df):
    # get user input for how many comparisons to make
    st.markdown("## Summary Statistics")

    # stats
    avg: float = df.amount.mean()
    sd: float = df.amount.std()
    unique_funds: int = df.fund_id.unique().size
    small: float = df.amount.min()
    big: float = df.amount.max()

    # table
    stats = {
        "Mean": [avg], "Standard Deviation": [sd], "Unique Funds": [unique_funds],
        "Smallest Donation": [small], "Largest Donation": [big]
    }
    stats_df = pd.DataFrame(stats)
    st.table(stats_df.style.format({
        "Mean": "{:.2f}", "Standard Deviation": "{:.2f}",
        "Smallest Donation": "{:.2f}", "Largest Donation": "{:.2f}"
    }))


