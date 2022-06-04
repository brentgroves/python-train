https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API#fast_executemany
https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5

New in version 4.0.19.) Simply adding

# crsr is a pyodbc.Cursor object
crsr.fast_executemany = True
can boost the performance of executemany operations by greatly reducing the number of round-trips to the server.

Notes:

This feature is "off" by default, and is currently only recommended for applications that use Microsoft's ODBC Driver for SQL Server.
The parameter values are held in memory, so very large numbers of records (tens of millions or more) may cause memory issues.
Writing fractional seconds of datetime.time values is supported, unlike normal pyodbc behavior
See this tip regarding fast_executemany and temporary tables.
For information on using fast_executemany with SQLAlchemy (and pandas) see the Stack Overflow question here.

Here, all the parameters are sent to the database server in one bundle (along with the SQL statement), and the database executes the SQL against all the parameters as one database transaction. Hence, this form of executemany() should be much faster than the default executemany(). However, there are limitations to it, see fast_executemany for more details.

Note, after running executemany(), the number of affected rows is NOT available in the rowcount attribute.

Under the hood, there is one important difference when fast_executemany=True. In that case, on the client side, pyodbc converts the Python parameter values to their ODBC "C" equivalents, based on the target column types in the database. E.g., a string-based date parameter value of "2018-07-04" is converted to a C date type binary value by pyodbc before sending it to the database. When fast_executemany=False, that date string is sent as-is to the database and the database does the conversion. This can lead to some subtle differences in behavior depending on whether fast_executemany is True or False.

