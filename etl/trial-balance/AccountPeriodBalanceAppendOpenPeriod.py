#!/miniconda/bin/python

#!/miniconda/bin/python
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python
#!/miniconda/bin/python # for docker image
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python # for debugging
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
    # username2 = (sys.argv[1])
    # password2 = (sys.argv[2])
    # username3 = (sys.argv[3])
    # password3 = (sys.argv[4])
    username2 = 'mgadmin' 
    password2 = 'WeDontSharePasswords1!' 
    username3 = 'root'
    password3 = 'password'
    # params = (sys.argv[1])
    # username = (sys.argv[2])
    # password = (sys.argv[3])
    # username2 = (sys.argv[4])
    # password2 = (sys.argv[5])
    # print(f"params={params}")
    # print(f"params={params},username={username},password={password},username2={username2},password2={password2}")
    # sys.exit(0)
    # https://geekflare.com/calculate-time-difference-in-python/
    start_time = datetime.now()
    end_time = datetime.now()

    current_time = start_time.strftime("%H:%M:%S")
    print_to_stdout(f"Current Time: {current_time=}")
    # https://www.pythonfixing.com/2022/02/fixed-how-to-set-db-connection-timeout.html
    conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw',timeout=30)
    # conn2.timeout = 10
    # conn2.autocommit = True
    cursor2 = conn2.cursor()

    
    # https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
    rowcount=cursor2.execute("{call Plex.account_period_balance_delete_open_period}").rowcount
    print_to_stdout(f"call Plex.account_period_balance_delete_open_period - rowcount={rowcount}")
    print_to_stdout(f"call Plex.account_period_balance_delete_open_period - messages={cursor2.messages}")
    cursor2.commit()

    rowcount=cursor2.execute("{call Plex.account_period_balance_append_open_period}").rowcount

    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # The return value is always the cursor itself:
    print_to_stdout(f"call Plex.account_period_balance_append_open_period - rowcount={rowcount}")
    print_to_stdout(f"call Plex.account_period_balance_append_open_period - messages={cursor2.messages}")
    cursor2.commit()
    cursor2.close()
    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API#fast_executemany
    # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
    # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5

    conn3 = mysql.connector.connect(user=username3, password=password3,
                              host='10.1.0.116',
                              port='31008',
                              database='Plex')

    cursor3 = conn3.cursor()

    cursor3.callproc('account_period_balance_delete_open_period', [])
    # rowcount=cursor2.execute(txt.format(dellist = params)).rowcount
    print_to_stdout(f"call Plex.account_period_balance_delete_open_period() - rowcount={cursor3.rowcount}")
    # print_to_stdout(f"{txt} - messages={cursor2.messages}")
    conn3.commit()

    cursor3.callproc('account_period_balance_append_open_period', [])
    # rowcount=cursor2.execute(txt.format(dellist = params)).rowcount
    print_to_stdout(f"call Plex.account_period_balance_append_open_period() - rowcount={cursor3.rowcount}")
    # print_to_stdout(f"{txt} - messages={cursor2.messages}")
    conn3.commit()
    cursor3.close()


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
    if 'conn2' in globals():
        conn2.close()
    if 'conn3' in globals():
        if conn3.is_connected():
            conn3.close()
            # print("MySQL connection is closed")
    sys.exit(ret)