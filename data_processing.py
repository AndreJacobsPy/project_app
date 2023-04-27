import pandas as pd


def simplify(data: pd.DataFrame) -> pd.DataFrame:
    column_structure = [
        ['Gf_Date', 'Gf_CnBio_ID', 'Gf_Fnds_1_01_Fund_ID',
         'Gf_Fnds_1_01_Description', 'Gf_Fnds_1_01_Amount'],
        ['Gf_Date', 'Gf_CnBio_ID', 'Gf_Fnds_1_02_Fund_ID',
         'Gf_Fnds_1_02_Description', 'Gf_Fnds_1_02_Amount'],
        ['Gf_Date', 'Gf_CnBio_ID', 'Gf_Fnds_1_03_Fund_ID',
         'Gf_Fnds_1_03_Description', 'Gf_Fnds_1_03_Amount']
    ]

    # new dataframe object, we will add to it
    tall_data = pd.DataFrame()
    for cols in column_structure:
        # some easy cleaning procedures
        temp = pd.DataFrame(data[cols])
        temp.columns = ["date", "const_id", "fund_id", "description", "amount"]
        temp = temp.dropna(subset=["amount"]).query("amount != 0")

        # adding to new DF
        tall_data = pd.concat([tall_data, temp])

        return tall_data


if __name__ == "__main__":
    # import data
    df = pd.read_excel("../EAB Gift 23Jan2023 copy.xlsx")
    new_df = simplify(df)

    # display data
    print(new_df.head())
    print(new_df.shape)
    print(new_df.dtypes)
    print(new_df.date.apply(lambda x: x.year))
