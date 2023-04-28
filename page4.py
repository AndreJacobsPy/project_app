import streamlit as st


def comparisons(data):
    # comparing different datetime sections
    st.markdown("## Time Comparisons")

    # get user input on how to subset data
    method = st.selectbox("Subset method", ["Year", "Month", "Weekday"])

    # group by chosen method
    if method == "Year":
        st.table(data.groupby(data.index.year).amount.mean())

    elif method == "Month":
        st.table(data.groupby(data.index.month).amount.mean())

    else:
        st.table(data.groupby(data.index.day_name()).amount.mean())
