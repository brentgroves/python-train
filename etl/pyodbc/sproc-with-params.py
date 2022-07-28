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

    pcn = '123681'
    username2 = 'mgadmin'
    password2 = 'WeDontSharePasswords1!'
    username3 = 'root'
    password3 = 'password'   


    conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw')

    cursor2 = conn2.cursor()

    tsql = """\
    declare @period_start_out int; 
    declare @period_end_out int;
    EXEC Plex.accounting_balance_get_period_range @pcn = ?,@period_start = @period_start_out OUTPUT,@period_end = @period_end_out OUTPUT;
    SELECT @period_start_out AS period_start, @period_end_out as period_end;
    """
    cursor2.execute(tsql, (123681))
    row = cursor2.fetchone()
    period_start = row[0];
    period_end= row[1]
    print(f"TSQL: period_start={period_start} period_end={period_end}")

    conn3 = mysql.connector.connect(user=username3, password=password3,
                            host='10.1.0.116',
                            port='31008',
                            database='Plex')

    cursor3 = conn3.cursor()
    plsql = """\
    call accounting_balance_get_period_range(123681,@period_start,@period_end);
    select @period_start period_start,@period_end period_end;
    """
    period_start2 = 0
    period_end2 = 0
    result_args =cursor3.callproc('accounting_balance_get_period_range', [pcn,period_start2,period_end2])
    # result_args =cursor3.callproc('accounting_balance_get_period_range', [123681,period_start2,period_end2])

#  https://www.mysqltutorial.org/calling-mysql-stored-procedures-python/
    # cursor3.execute(plsql, [])
    # row = cursor3.fetchone()
    # period_start = row[0];
    # period_end= row[1]
    print(f"PLSQL: period_start={result_args[1]} period_end={result_args[2]}")

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
    if 'conn2' in globals():
        conn2.close()
    if 'conn3' in globals():
        conn3.close()
