https://www.geeksforgeeks.org/python-output-formatting/
# Python program showing
# use of format() method
 
# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
 
# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
 
print('{1} and {0}'.format('Geeks', 'Portal'))
 
 
# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.
 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
 
# using format() method and referring
# a position of the object
print(f"{'Geeks'} and {'Portal'}")

MY_TABLE = 'some_tbl'

conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                      server='MYSERVER',
                      database='MYDB',
                      uid='MYUSER', pwd='MYPASSWORD')

insert_to_tmp_tbl_stmt = f"INSERT INTO {MY_TABLE} VALUES (?,?,?,?,?,?)"

# standard
cursor.execute("select a from tbl where b=? and c=?", (x, y))
# pyodbc extension
cursor.execute("select a from tbl where b=? and c=?", x, y)

# Python program showing
# a use of format() method
 
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))
 
# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))
 
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))
 
print("Geeks: {a:5d},  Portal: {p:8.2f}".
     format(a = 453, p = 59.058))