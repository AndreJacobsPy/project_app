import pandas as pd
import streamlit as st
import plotly.express as px


def graphs(grouped, method: str):
    data = pd.DataFrame(grouped).reset_index()
    data.columns = [method, "Donation Amount"]
    fig = px.bar(
        data, method, "Donation Amount", title="Donations by {}".format(method)
    )
    return fig


def comparisons(data):
    # comparing different datetime sections
    st.markdown("## Time Comparisons")

    # get user input on how to subset data
    method = st.selectbox("Subset method", ["Year", "Month", "Weekday"])

    # group by chosen method
    if method == "Year":
        groups = data.groupby(data.index.year).amount.mean()

    elif method == "Month":
        groups = data.groupby(data.index.month).amount.mean()

    else:
        groups = data.groupby(data.index.day_name()).amount.mean()

    st.table(groups)
    fig = graphs(groups, method)

    st.markdown("## Distribution of Donations")
    st.plotly_chart(fig)
