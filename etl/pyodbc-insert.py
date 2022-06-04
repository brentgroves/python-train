import pyodbc
import pandas as pd
# https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
df = pd.read_csv('myfile.csv')
MY_TABLE = 'some_tbl'

conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                      server='MYSERVER',
                      database='MYDB',
                      uid='MYUSER', pwd='MYPASSWORD')

insert_to_tmp_tbl_stmt = f"INSERT INTO {MY_TABLE} VALUES (?,?,?,?,?,?)"
cursor = conn.cursor()
cursor.fast_executemany = True
cursor.executemany(insert_to_tmp_tbl_stmt, df.values.tolist())
print(f'{len(df)} rows inserted to the {MY_TABLE} table')
cursor.commit()
cursor.close()
conn.close()