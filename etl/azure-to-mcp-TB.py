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

    pcn_list = '123681,300758'
    period_start = '202101'
    period_end = '202206'
    username2 = 'mgadmin'
    password2 = 'WeDontSharePasswords1!'
    username3 = 'root'
    password3 = 'password'
    # print(f"params={params}")
    # print(f"params={params},username={username},password={password},username2={username2},password2={password2}")

    start_time = datetime.now()
    end_time = datetime.now()

    current_time = start_time.strftime("%H:%M:%S")
    print_to_stdout(f"Current Time: {current_time=}")

    conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw')
    cursor2 = conn2.cursor()

    select_statement =f'''select 
    pcn,account_no,period,period_display
    ,debit,ytd_debit,credit,ytd_credit
    ,balance,ytd_balance
    from Plex.account_period_balance  
    where pcn in ({pcn_list})
    and period between {period_start} and {period_end}'''
    # print(select_statement)

    cursor2.execute(select_statement)
    rows = cursor2.fetchall()
    cursor2.close()

    print_to_stdout(f"{select_statement} - rowcount={len(rows)}")

    fetch_time = datetime.now()
    tdelta = fetch_time - start_time 
    print_to_stdout(f"fetch_time={tdelta}") 

    insertList = []
    # columnNames = [column[0] for column in cursor.description]
    for record in rows:
      insertList.append(tuple(record))

    conn3 = mysql.connector.connect(user=username3, password=password3,
                              host='10.1.0.116',
                              port='31008',
                              database='Azure')
    # conn3 = mysql.connector.connect(user='root', password='password',
    #                           host='10.1.0.116',
    #                           port='31008',
    #                           database='mcpdw')

    cursor3 = conn3.cursor()
    # https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
    # txt = "delete from Plex.accounting_account where pcn in ({dellist:s})"
    delete_statement = "delete from Azure.account_period_balance"
    # https://github.com/mkleehammer/pyodbc/wiki/Cursor
    # The return value is always the cursor itself:
    cursor3.execute(delete_statement)
    # rowcount=cursor2.execute(txt.format(dellist = params)).rowcount
    print_to_stdout(f"{delete_statement} - rowcount={cursor3.rowcount}")
    # print_to_stdout(f"{txt} - messages={cursor2.messages}")

    conn3.commit()

    im2 = '''insert into Azure.account_period_balance (pcn,account_no,period,period_display,debit,ytd_debit,credit,ytd_credit,balance,ytd_balance)    
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

    cursor3.executemany(im2,insertList)
    # cursor2.executemany(im2,records_to_insert)
    conn3.commit()
    cursor3.close()

    # https://geekflare.com/calculate-time-difference-in-python/
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
    # end_time = datetime.now()
    # tdelta = end_time - start_time 
    # print_to_stdout(f"total time: {tdelta}") 
    # if 'conn' in globals():
    #     conn.close()
    if 'conn2' in globals():
        conn2.close()
    if 'conn3' in globals():
        if conn3.is_connected():
            conn3.close()
            # print("MySQL connection is closed")
    sys.exit(ret)
