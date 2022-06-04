import pyodbc 
from datetime import datetime
import sys 
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/programming-guidelines?view=sql-server-ver16
# remember to source oaodbc64.sh to set env variables.
# remember to source oaodbc64.sh to set env variables.
# remember to source oaodbc64.sh to set env variables.
# https://github.com/mkleehammer/pyodbc/wiki/Calling-Stored-Procedures
# https://thepythonguru.com/fetching-records-using-fetchone-and-fetchmany/
# https://code.google.com/archive/p/pyodbc/wikis/Cursor.wiki
def print_to_stdout(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stdout)

def print_to_stderr(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stderr)
    # InterfaceError('IM002', '[IM002] [unixODBC][Driver Manager]Data source name not found and no default driver specified (0) (SQLDriverConnect)')
try:
# https://geekflare.com/calculate-time-difference-in-python/
    start_time = datetime.now()

    current_time = start_time.strftime("%H:%M:%S")
    print("Current Time =", current_time)    
    ret = 0
    # https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15
    username = 'mg.odbcalbion' 
    # password = 'wrong' 
    password = 'Mob3xalbion' 
    conn = pyodbc.connect('DSN=Plex;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DSN=Plex;UID='+username+';PWD='+ password)
    # server = 'tcp:mgsqlmi.public.48d444e7f69b.database.windows.net,3342' 
    # database = 'mgdw' 
    # username = 'mgadmin' 
    # password = 'WeDontSharePasswords1!' 
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    # https://stackoverflow.com/questions/11451101/retrieving-data-from-sql-using-pyodbc
    cursor = conn.cursor()
    #Sample select query
    # params = ("123681")
    params = ("123681,300758,310507,306766,300757")
    cursor.execute("{call sproc300758_11728751_1978024 (?)}", params)

    username = 'mgadmin' 
    password = 'WeDontSharePasswords1!' 
    conn2 = pyodbc.connect('DSN=dw;UID='+username+';PWD='+ password + ';DATABASE=mgdw')

    cursor2 = conn2.cursor()
    im2='''insert into Scratch.accounting_account_06_03
    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' 
    rec = [(123681,629753,'10000-000-00000','Cash - Comerica General',0,'Asset',0,'category-name-legacy','cattypeleg',0,'subcategory-name-legacy','subcattleg',0,201604)]
    print(im2)
    # cursor2.executemany(im2,rows)
    # cursor2.executemany(im2,rec)
    # print("Length=% s" % len(list))
    print("cursor.rowcount=%s" % cursor.rowcount)
    number_of_fetches=0
    while True:
        # rows = cursor.fetchmany(1000)  # 2 min 39 seconds
        rows = cursor.fetchmany(5000)
        if not rows:
            break
        # print(rows)
        number_of_fetches=number_of_fetches+1
        cursor2.executemany(im2,rows)


    # if 'cursor' in globals():
    #     cursor.close()
    # if 'conn' in globals():
    #     conn.close()

    #Sample select query
    # cursor2.execute("SELECT @@version;") 
    # row = cursor2.fetchone() 
    # while row: 
    #     print(row[0])
    #     row = cursor2.fetchone()


    # username = 'mgadmin' 
    # # password = 'BadPassword' 
    # password = 'WeDontSharePasswords1!' 
    # conn = pyodbc.connect('DSN=dw;UID='+username+';PWD='+ password + ';DATABASE=mgdw')

    # cursor = conn.cursor()

    # ins ='''insert into Validation.Detailed_Production_History_test (pcn,production_no,part_no,part_key,record_date)
    # values (?,?,?,?,?)'''
    # print_to_stdout(ins)

    # rec=[]
    # cursor.executemany(ins,rec)
    # # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5

except pyodbc.Error as ex:
    ret = 1
    # print(ex) 
    # sqlstate = ex.args[0]
    # print(sqlstate) 
    error_msg = ex.args[1]
    print_to_stderr(error_msg) 
#   print_to_stdout("std out message") 
# except pyodbc.Error as ex:
#   ret = 1
#   # print('exception')
#   print_to_stdout("std out message") 
#   print_to_stderr("ODBC connection error.") 

finally:
    end_time = datetime.now()
    tdelta = end_time - start_time 
    print(tdelta) 
    print(type(tdelta)) 

    if 'cursor' in globals():
        # cursor.commit()
        cursor.close()
    if 'conn' in globals():
        conn.close()
    #   sys.exit(ret)
    if 'cursor2' in globals():
        cursor2.commit()
        cursor2.close()
    if 'conn2' in globals():
        conn2.close()
