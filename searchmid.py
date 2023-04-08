import pandas as pd

df = pd.read_excel('assets/MidtermScores.xlsx', index_col='Student_number')

def get_value(Student_number):
    try:
        return df.loc[Student_number]['Total']
    except KeyError:
        return None

if __name__ == '__main__':
    import cgi

    form = cgi.FieldStorage()
    Student_number = form.getvalue('Student_number')

    value = get_value(Student_number)

    if value is None:
        print('Error: ID number not found')
    else:
        print(value)
