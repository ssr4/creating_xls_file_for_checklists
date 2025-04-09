import pandas as pd


if __name__ == "__main__":
    try:
        df = pd.read_excel('new_example.xlsx', sheet_name='Sheet1')
        new_df = df.copy()
        new_df.to_excel('new_template.xlsx', index=False)
    except Exception as e:
        print(' Error: ', e)
