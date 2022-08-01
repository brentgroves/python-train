# https://docs.python-zeep.org/en/master/
#import xmltodict
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport
import pyodbc
import logging.config

# https://docs.python-zeep.org/en/master/transport.html?highlight=authentication#http-authentication
session = Session()
session.auth = HTTPBasicAuth('MGEdonReportsws@plex.com','9f45e3d-67ed-')

client = Client(wsdl='Plex_SOAP_prod.wsdl',transport=Transport(session=session))
# https://docs.python-zeep.org/en/master/datastructures.html
e_type = client.get_type('ns0:ExecuteDataSourceRequest')
a_ip_type = client.get_type('ns0:ArrayOfInputParameter')
ip_type=client.get_type('ns0:InputParameter')
pcn = ip_type(Value='123681',Name='@PCNs',Required=False,Output=False)
period_start = ip_type(Value='202207',Name='@Period_Start',Required=True,Output=False)
period_end = ip_type(Value='202207',Name='@Period_End',Required=True,Output=False)

# Report_Date=ip_type(Value='2022-04-28 08:00:00',Name='@Report_Date',Required=False,Output=False)
# End_Date=ip_type(Value='2022-04-28 08:59:59',Name='@End_Date',Required=False,Output=False)


Parameters=a_ip_type([pcn,period_start,period_end])

# e=e_type(DataSourceKey=8619,InputParameters=[{'Value':'4/26/2022','Name':'@Report_Date','Required':False,'Output':False}],DataSourceName='Detailed_Production_Get_New')
e=e_type(DataSourceKey=4814,InputParameters=Parameters,DataSourceName='Account_Activity_Summary_xPCN_Get')


response = client.service.ExecuteDataSource(e)
# print(response['OutputParameters'])

column_list = response['ResultSets'].ResultSet[0].Rows.Row[0].Columns.Column
column_names=""
column_values=""
dic ={}
ind=0
for j in column_list:
  dic.update({j.Name:ind}) 
  print(str(ind) + '-' + j.Name)
  ind=ind+1

print(dic)

# print(rec)
list = response['ResultSets'].ResultSet[0].Rows.Row
pcn = 123681
period = 202207
rec=[]
row=0
for i in list:
  # rec.append((rs.Columns.Column[0].Value))
  # rec = [(rs.Columns.Column[0].Value)]
  rec.append((pcn,period,i.Columns.Column[1].Value,i.Columns.Column[4].Value,i.Columns.Column[5].Value,i.Columns.Column[6].Value,i.Columns.Column[7].Value))
# rec.append((rs.Columns.Column[2].Value,rs.Columns.Column[5].Value))
  # print(rec[row])
  # row=row+1

try:
#server = 'tcp:mgsqlmi.public.48d444e7f69b.database.windows.net,3342' 
# database = 'mgdw' 
  username = 'mgadmin' 
  password = 'WeDontSharePasswords1!' 
  conn = pyodbc.connect('DSN=dw;UID='+username+';PWD='+ password + ';DATABASE=mgdw')

  cursor = conn.cursor()
  ins ='''insert into Plex.account_activity_summary_xpcn_get (pcn,period,account_no,beginning_balance,debit,credit,ending_balance)
  values (?,?,?,?,?,?,?)'''

  cursor.fast_executemany = True

  cursor.executemany(ins,rec)

except pyodbc.Error as ex:
  # exception.PyODBCError(ex)  
  sqlstate = ex.args[0]
  # if sqlstate == '28000':
  #     print("LDAP Connection failed: check password")

finally:
  cursor.commit()
  cursor.close()
  conn.close()
# # insert into Validation.detailed_production_history
# # values
# # print(response['ResultSets'].ResultSet[0].Rows.Row[100].Columns.Column[0].Value)
# # print(response['ResultSets'].ResultSet[0].Rows.Row[100].Columns.Column[0].Value)

# for word in response:
#     print(word)

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