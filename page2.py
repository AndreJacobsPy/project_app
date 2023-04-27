import streamlit as st
import pandas as pd
import calendar


# import data
# import data and fix it
def second_page(data: pd.DataFrame):
    # create user input section
    df = data.copy()
    year_, month_, day_, weekday_ = st.columns(4)

    with year_:
        year = st.checkbox("Year")
        year_value = st.number_input("Year",
                                     min_value=df.index.year.min(), max_value=df.index.year.max()
                                     )

        if year:
            df = df.query(f"index.dt.year == {year_value}")

    with month_:
        month = st.checkbox("Month")
        month_value = st.number_input("Month", min_value=1, max_value=12)

        if month:
            df = df.query(f"index.dt.month == {month_value}")

    with day_:
        day = st.checkbox("Day")
        day_value = st.number_input("Day", min_value=1, max_value=31)

        if day:
            df = df.query(f"index.dt.day == {day_value}")

    with weekday_:
        weekday = st.checkbox("Weekday")
        weekday_value = st.selectbox("Weekday",
                                     ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                      "Saturday", "Sunday"])

        if weekday:
            df = df.reset_index()
            df = df[df["date"].dt.day_name() == weekday_value]

    # filter data
    st.table(df.head(10))


if __name__ == "__main__":
    frame = pd.read_excel("/Users/andrejacobs/Desktop/una_data/EAB Gift 23Jan2023 copy.xlsx")
    second_page(frame)