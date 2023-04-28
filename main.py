import streamlit as st
from page1 import load_data
from page2 import filterer
from page3 import stats_table
from page4 import comparisons
from page5 import user_comparisons


# app start!
st.markdown("# Datetime Fund Analysis")

# adding tabs for different pages
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Upload", "Summary", "Stats", "Comparison", "UserComparisons"])

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
        st.table(df)

# third page
with tab3:
    if file is not None:
        stats_table(df)

# fourth page
with tab4:
    if file is not None:
        comparisons(df)

# fifth page
with tab5:
    if file is not None:
        user_comparisons(df)
