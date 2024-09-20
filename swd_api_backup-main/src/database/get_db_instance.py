import pyodbc

database = 'SWDProject'
uid = 'sa'
password = '12345'

connectionString = 'Driver={SQL Server};Server=(local);Database='+database+';UID='+uid+';PWD='+password+';'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()






