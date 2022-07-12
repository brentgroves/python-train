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
    # params = (sys.argv[1])
    # username = (sys.argv[2])
    # password = (sys.argv[3])
    # username2 = (sys.argv[4])
    # password2 = (sys.argv[5])
    # username3 = (sys.argv[6])
    # password3 = (sys.argv[7])

    params = '123681,300758'
    username = 'mg.odbcalbion'
    password = 'Mob3xalbion'
    username2 = 'mgadmin'
    password2 = 'WeDontSharePasswords1!'
    username3 = 'root'
    password3 = 'password'    # print(f"params={params}")
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
    
    rowcount=cursor.execute("{call sproc300758_11728751_1999565 (?)}", params)
    rows = cursor.fetchall()
    print_to_stdout(f"call sproc300758_11728751_1999565 - rowcount={rowcount}")
    print_to_stdout(f"call sproc300758_11728751_1999565 - messages={cursor.messages}")

    cursor.close()
    fetch_time = datetime.now()
    tdelta = fetch_time - start_time 
    print_to_stdout(f"fetch_time={tdelta}") 

    if len(rows):
        conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw')
        cursor2 = conn2.cursor()
        # https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
        del_command = f"delete from Plex.accounting_balance_update_period_range where pcn in ({params})"
        # del_command = f"delete from Scratch.accounting_balance_update_period_range where pcn in ({params})"
        # https://github.com/mkleehammer/pyodbc/wiki/Cursor
        # The return value is always the cursor itself:
        rowcount=cursor2.execute(del_command).rowcount
        print_to_stdout(f"{del_command} - rowcount={rowcount}")
        print_to_stdout(f"{del_command} - messages={cursor2.messages}")

        cursor2.commit()

        # https://github.com/mkleehammer/pyodbc/wiki/Cursor
        # https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API#fast_executemany
        # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
        im2='''insert into Plex.accounting_balance_update_period_range (pcn,period_start,period_end)  
                values (?,?,?)''' 
        cursor2.fast_executemany = True
        cursor2.executemany(im2,rows)
        # https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
        cursor2.commit()
        cursor2.close()
 
        insertObject = []
        # columnNames = [column[0] for column in cursor.description]
        for record in rows:
            insertObject.append(tuple(record))

        conn3 = mysql.connector.connect(user=username3, password=password3,
                                host='10.1.0.116',
                                port='31008',
                                database='Plex')
        cursor3 = conn3.cursor()
        # https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
        del_command = f"delete from Plex.accounting_balance_update_period_range where pcn in ({params})"
        cursor3.execute(del_command)
        # rowcount=cursor2.execute(txt.format(dellist = params)).rowcount
        print_to_stdout(f"{del_command} - rowcount={cursor3.rowcount}")
        # print_to_stdout(f"{txt} - messages={cursor2.messages}")
        conn3.commit()
        im2='''insert into Plex.accounting_balance_update_period_range (pcn,period_start,period_end)  
                values (%s,%s,%s)''' 
        cursor3.executemany(im2,insertObject)
        # cursor2.executemany(im2,records_to_insert)
        conn3.commit()
        cursor3.close()

except pyodbc.Error as ex:
    ret = 1
    error_msg = ex.args[1]
    print_to_stderr(f"error {error_msg}") 
    print_to_stderr(f"error {ex.args}") 

except Error as e:
    ret = 1
    print("MySQL error: ", e)

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
    sys.exit(ret)
