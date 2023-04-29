import streamlit as st
from plotly import express as px


def graphs(grouped, method):
    fig = px.bar(
        grouped.index, grouped, title="Donations by {}".format(method),
        labels={"Index": method, "x": "donation amount"}
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
