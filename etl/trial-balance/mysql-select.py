import mysql.connector
# 10.1.0.116 / 31008
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
# - mysql-connector-python=8.0.18  
# conda install -c anaconda mysql-connector-python
cnx = mysql.connector.connect(user='root', password='password',
                              host='10.1.0.116',
                              port='31008',
                              database='test')
cursor = cnx.cursor()
query = ("select * from mytable")
# query = ("SELECT first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
cursor.execute(query)

# https://pynative.com/python-mysql-insert-data-into-database-table/#h-insert-multiple-rows-into-mysql-table-using-the-cursor-s-executemany
for (c) in cursor:
  print("{} in mytable".format(
    c))

# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))


cursor.close()
cnx.close()