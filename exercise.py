
 
import MySQLdb 
 
db = my.connect(host="192.168.200.130",
user="sa",
passwd="gmtonline",
db="ebizos_db_201802060600"
)
 
print(db)
 
cursor = db.cursor()
 
number_of_rows = cursor.execute("select * from temperaturedata");
 
print(number_of_rows)