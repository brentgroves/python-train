#!/miniconda/bin/python

#!/miniconda/bin/python
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python
#!/miniconda/bin/python # for docker image
#!/home/bgroves@BUSCHE-CNC.COM/anaconda3/bin/python # for debugging

import string
import sys
from datetime import datetime, timedelta

import mysql.connector
import pyodbc
from mysql.connector import Error
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
# https://docs.python-zeep.org/en/master/
#import xmltodict
from zeep import Client
from zeep.transports import Transport


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
  # pcn = (sys.argv[1])
  # username2 = (sys.argv[2])
  # password2 = (sys.argv[3])
  # username3 = (sys.argv[4])
  # password3 = (sys.argv[5])
  # username4 = (sys.argv[6])
  # password4 = (sys.argv[7])

  pcn = '123681'
  # pcn = '300758'
  username2 = 'mgadmin' 
  password2 = 'WeDontSharePasswords1!' 
  username3 = 'root'
  password3 = 'password'
  # username4 = 'MGEdonReportsws@plex.com'
  # password4 = '9f45e3d-67ed-'
  username4 = 'MGAlbionReportsws@plex.com'
  password4 = '697fd42-084c-'

  # Get today's date
  today = datetime.today()

  # Yesterday date
  yesterday = today - timedelta(days = 1)
  report_date=yesterday.strftime("%Y-%m-%d")+' 00:00:00'
#  report_date=yesterday.strftime("%m/%d/%Y")+' 00:00:00'


  conn2 = pyodbc.connect('DSN=dw;UID='+username2+';PWD='+ password2 + ';DATABASE=mgdw',timeout=30)
  # conn2.timeout = 10
  # conn2.autocommit = True
  cursor2 = conn2.cursor()

  # https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
  sql ='''
  delete from DailyMetrics.daily_shift_report_debug
  WHERE pcn = ? and report_date = ?
  '''.replace('\n', ' ')

  rowcount=cursor2.execute(sql, (pcn,report_date)).rowcount
  print_to_stdout(f"{sql} - rowcount={rowcount}")
  print_to_stdout(f"{sql} - messages={cursor2.messages}")
  cursor2.commit()

  # debug section
#   sql ='''
#   insert into DailyMetrics.daily_shift_report 
#   (pcn,report_date,workcenter_key,workcenter_code,part_key,part_no,part_revision,
#    part_name,operation_no,operation_code,parts_produced,parts_scrapped,
#    earned_hours,actual_hours,part_operation_key,quantity_produced,labor_rate)
#   values ('123681', '08/10/2022 00:00:00', '58321', 'CD4 RH Pack', '2684942', 'H2GC 5K651 AB', '', 'CD4.2 RH', '120', 'Final', '370', '0', '3.854167', '20.65834', '7471212', '370', '48')'''
#   rowcount=cursor2.execute(sql).rowcount
#   print_to_stdout(f"{sql} - rowcount={rowcount}")
#   print_to_stdout(f"{sql} - messages={cursor2.messages}")
#   cursor2.commit()

#   im2 ='''insert into DailyMetrics.daily_shift_report_debug 
#   (pcn,report_date)
#   values (?,?)'''

  # test = rec[0:500]
  cursor2.fast_executemany = True
  cursor2.executemany(im2,[('1',report_date)]) 
#   cursor2.executemany(im2,[('123681', '08/10/2022 00:00:00', '58321', 'CD4 RH Pack', '2684942', 'H2GC 5K651 AB', '', 'CD4.2 RH', '120', 'Final', '370', '0', '3.854167', '20.65834', '7471212', '370', '48')]) 
  cursor2.commit()
  cursor2.close()


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
    if 'conn2' in globals():
        conn2.close()
    if 'conn3' in globals():
        if conn3.is_connected():
            conn3.close()
            # print("MySQL connection is closed")
    sys.exit(ret)

# #python -mzeep Plex_SOAP_test.wsdl
# # https://www.youtube.com/watch?v=JBYEQjg_znI
# # request = '<ExecuteDataSourceRequest xmlns="http://www.plexus-online.com/DataSource"><DataSourceKey>8619</DataSourceKey><InputParameters><InputParameter><Value>4/26/2022</Value><Name>@Report_Date</Name><Required>false</Required><Output>false</Output></InputParameter></InputParameters><DataSourceName>Detailed_Production_Get_New</DataSourceName></ExecuteDataSourceRequest>'

# # request = '''<ExecuteDataSourceRequest xmlns="http://www.plexus-online.com/DataSource">
# #     <DataSourceKey>8619</DataSourceKey>
# #     <InputParameters>
# #       <InputParameter>
# #         <Value>4/26/2022</Value>
# #         <Name>@Report_Date</Name>
# #         <Required>false</Required>
# #         <Output>false</Output>
# #       </InputParameter>
# #     </InputParameters>
# #     <DataSourceName>Detailed_Production_Get_New</DataSourceName>
# #   </ExecuteDataSourceRequest>'''
# # print(request)
# # client.service.ExecuteDataSource(request)
