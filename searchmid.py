import pandas as pd

df = pd.read_excel('MidtermScores.xlsx', index_col='Student_number')

def get_value(Student_number):
    try:
        return df.loc[Student_number]['Total']
    except KeyError:
        return None
