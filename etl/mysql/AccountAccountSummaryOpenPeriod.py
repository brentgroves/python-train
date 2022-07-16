#!/miniconda/bin/python

#!/miniconda/bin/python # for docker image
#!/miniconda/bin/python
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python # for debugging
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python
# https://docs.python-zeep.org/en/master/
import pyodbc 
from datetime import datetime
import sys 
import mysql.connector
from mysql.connector import Error

# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/programming-guidelines?view=sql-server-ver16
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
    ret = 0
    PCNList = '123681'
    PeriodOffset = 0
    
    username = 'mg.odbcalbion'
    password = 'Mob3xalbion'
    # username = 'MGAlbionReportsws@plex.com' DOES NOT WORK
    # password = '697fd42-084c-'
    username2 = 'mgadmin'
    password2 = 'WeDontSharePasswords1!'
    username3 = 'root'
    password3 = 'password'

    # The following parameters always have the same value
    ExcludePeriod13 = 0
    ExcludePeriodAdjustments = 0
    # params = (sys.argv[1])
    # username = (sys.argv[2])
    # password = (sys.argv[3])
    # username2 = (sys.argv[4])
    # password2 = (sys.argv[5])
    # username3 = (sys.argv[6])
    # password3 = (sys.argv[7])

    # print(f"params={params}")
    # print(f"params={params},username={username},password={password},username2={username2},password2={password2}")
    # sys.exit(0)
    # https://geekflare.com/calculate-time-difference-in-python/
    start_time = datetime.now()
    end_time = datetime.now()

    current_time = start_time.strftime("%H:%M:%S")
    print_to_stdout(f"Current Time: {current_time=}")

    # https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15
    # password = 'wrong' 
    conn = pyodbc.connect('DSN=Plex;UID='+username+';PWD='+ password)
    # https://stackoverflow.com/questions/11451101/retrieving-data-from-sql-using-pyodbc
    cursor = conn.cursor()

    cursor.execute("{call sproc123681_11728751_2087993(?,?,?,?)}", PCNList)
    rows = cursor.fetchall()

    cursor.close()
    fetch_time = datetime.now()
    tdelta = fetch_time - start_time 
    print_to_stdout(f"fetch_time={tdelta}") 

    # https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
    # elf-contained driver. Connector/Python does not require the MySQL client library or any Python modules outside the standard library.
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

    conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw')

    cursor2 = conn2.cursor()
    rowcount=cursor2.execute("{call Plex.accounting_account_summary_delete_open_period}").rowcount
    # rowcount=cursor2.execute("{call Scratch.account_period_balance_delete_period_range}").rowcount
    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # The return value is always the cursor itself:
    print_to_stdout(f"call Plex.accounting_account_summary_delete_open_period - rowcount={rowcount}")
    print_to_stdout(f"call Plex.accounting_account_summary_delete_open_period - messages={cursor2.messages}")
    cursor2.commit()

    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API#fast_executemany
    # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5

    im2='''insert into Plex.accounting_account_summary_open_period(pcn,period,account_no,debit,credit,net)
    values (?,?,?,?,?,?)''' 
    # rec = [(123681,629753,'10000-000-00000','Cash - Comerica General',0,'Asset',0,'category-name-legacy','cattypeleg',0,'subcategory-name-legacy','subcattleg',0,201604)]
    cursor2.fast_executemany = True
    cursor2.executemany(im2,rows)
    cursor2.commit()
    cursor2.close()

    insertObject = []
    # columnNames = [column[0] for column in cursor.description]
    for record in rows:
      insertObject.append(tuple(record))

    # conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw')

    conn3 = mysql.connector.connect(user=username3, password=password3,
                              host='10.1.0.116',
                              port='31008',
                              database='Plex')
    # conn3 = mysql.connector.connect(user='root', password='password',
    #                           host='10.1.0.116',
    #                           port='31008',
    #                           database='mcpdw')

    cursor3 = conn3.cursor()
    # cursor2.callproc('get_laptop', [1, ])
    cursor3.callproc('accounting_account_summary_delete_open_period', [])
    # rowcount=cursor2.execute(txt.format(dellist = params)).rowcount
    print_to_stdout(f"call Plex.accounting_account_summary_delete_open_period() - rowcount={cursor3.rowcount}")
    # print_to_stdout(f"{txt} - messages={cursor2.messages}")
    conn3.commit()

    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API#fast_executemany
    # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
    im2 = """insert into Plex.accounting_account_summary_open_period(pcn,period,account_no,debit,credit,net)
                VALUES (%s,%s,%s,%s,%s,%s) """
 
    cursor3.executemany(im2,insertObject)
    # cursor2.executemany(im2,records_to_insert)
    conn3.commit()
    cursor3.close()

    # cursor2.executemany(im2,insertObject)
    # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
# Error while connecting to MySQL Failed executing the operation; Could not process parameters: 
# Row((123681, 629753, '10000-000-00000', 'Cash - Comerica General', 0, 'Asset', 0, '', '', 0, '', '', 0, 201604)), 
# it must be of type list, tuple or dict
except pyodbc.Error as ex:
    ret = 1
    error_msg = ex.args[1]
    print_to_stderr(error_msg) 

except Error as e:
    ret = 1
    print("Error while connecting to MySQL", e)

except BaseException as error:
    ret = 1
    print('An exception occurred: {}'.format(error))

finally:
    end_time = datetime.now()
    tdelta = end_time - start_time 
    print_to_stdout(f"total time: {tdelta}") 
    if 'conn' in globals():
        conn.close()
    if 'conn2' in globals():
        conn2.close()
    if 'conn3' in globals():
        if conn3.is_connected():
            conn3.close()
            # print("MySQL connection is closed")
    sys.exit(ret)
