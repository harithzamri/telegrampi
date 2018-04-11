
 
import pyodbc

try :
    db = pyodbc.connect("Driver = ODBC Driver 17 for SQL Server;"
		"Server = 192.168.200.130;"
		"UID=sa;"
		"PWD=gmtonline:"
		"Database=ebizos_db_201802060600;")

        cursor=db.cursor()
except Exception as e:
    print("error",str(e))
    



