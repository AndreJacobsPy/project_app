import streamlit as st
import pandas as pd
from page1 import load_data
from page2 import filterer, convert_df
from page3 import stats_table
from page4 import comparisons


# app start!!
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
    if file is not None:    
        # page title
        st.markdown("## Summary Statistics")

        # a function to help create multiple subsets
        def task(df: pd.DataFrame):
            # display data
            df = df.query(f"'{start}' <= index <= '{end}'").sort_index()
            return df

        # getting user input for how many subsets to do
        subsets = st.number_input("Subsets", step=1)
        
        for i in range(subsets):
        
            # making page pretty    
            col1, col2 = st.columns(2)

            # have to update widget name
            s_name = f"Start.{i+1}"
            e_name = f"End.{i+1}"

            # putting start and end date next to each other
            with col1:    
                start = st.date_input(s_name, value=df.index.max(), min_value=df.index.min(), max_value=df.index.max())
            
            with col2:
                end = st.date_input(e_name, value=df.index.max(), min_value=df.index.min(), max_value=df.index.max())

            st.table(stats_table(task(df)))
