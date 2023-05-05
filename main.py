import streamlit as st
import pandas as pd
from page1 import load_data
from page2 import filterer, convert_df
from page3 import stats_table
from page4 import comparisons


# app start!
st.markdown("# Datetime Fund Analysis")

# adding tabs for different pages
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Upload", "Summary", "Stats", "Comparison", "Subsets"])

# first page
with tab1:
    # file uploader widget
    file = st.file_uploader("Upload File")
    filetype = st.selectbox("Filetype", ["xlsx", "csv"])

    if file is not None:
        df = load_data(file, filetype)

# second page
with tab2:
    if file is not None:
        df = filterer(df)
        st.table(df.head(10))

        # download file
        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )

# third page
with tab3:
    if file is not None:
        st.markdown("## Summary Statistics")
        st.table(stats_table(df))

# fourth page
with tab4:
    if file is not None:
        comparisons(df)

# fifth page
with tab5:
    # page title
    st.markdown("## Summary Statistics")

    # a function to help create multiple subsets
    def task(df: pd.DataFrame):
        # display data
        df = df.query(f"index.dt.year == {year} & index.dt.month == {month}")
        return df

    # getting user input for how many subsets to do
    subsets = st.number_input("Subsets", step=1)
    years_: pd.DatetimeIndex = df.index.year

    for i in range(subsets):
        # change name
        name_m: str = f"month{i+1}"
        name_y: str = f"year{i+1}"

        # create widgets
        year: int = st.number_input(name_y, min_value=years_.min(), max_value=years_.max())
        month: int = st.number_input(name_m, min_value=1, max_value=12)

        # save data
        st.table(stats_table(task(df)))
        


