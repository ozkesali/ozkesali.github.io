import pandas as pd

df = pd.read_excel('site.xlsx', index_col='idnumber')

def get_value(idnumber):
    try:
        return df.loc[idnumber]['value']
    except KeyError:
        return None
