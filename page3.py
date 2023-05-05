import streamlit as st
import pandas as pd


def stats_table(df: pd.DataFrame):
    # stats
    avg: float = df.amount.mean()
    sd: float = df.amount.std()
    unique_funds: int = df.fund_id.unique().size
    small: float = df.amount.min()
    big: float = df.amount.max()
    number_donations: int = df.amount.count()

    # table
    stats = {
        "Mean": [avg], "Standard Deviation": [sd], "Unique Funds": [unique_funds],
        "Number of Donations": [number_donations], "Smallest Donation": [small], "Largest Donation": [big]
    }
    stats_df = pd.DataFrame(stats)
    return pd.DataFrame(stats_df.style.format({
        "Mean": "{:.2f}", "Standard Deviation": "{:.2f}",
        "Smallest Donation": "{:.2f}", "Largest Donation": "{:.2f}"
    }))


