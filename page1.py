import pandas as pd
import streamlit as st
from data_processing import simplify


# function for the first page of app
@st.cache_data
def load_data(file, filetype) -> pd.DataFrame:
    # checking for common file types
    if filetype == "xlsx":
        if file is not None:
            df = pd.read_excel(file)

    elif filetype ==  "csv":
        if file is not None:
            df = pd.read_csv(file)

    df = simplify(df).set_index("date")
    st.table(df.head())

    return df


if __name__ == "__main__":
    pass
