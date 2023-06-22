#CSV to MYsql
#Librerias
#py -m pip install mysql-connector-python
import pandas as pd
import mysql.connector

path = "C:\\Users\H473815\OneDrive - Honeywell\Proyectos\Migracion a I 4.0\CSV to BD\data\Reporte HC Diario.csv"
hcData = pd.read_csv(path, header=0, encoding="latin-1")
print(hcData.head(10))

"""
from MySQL.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  password='')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("Select * from myapp")
        print("Database is created")

except Error as e:
    print("Error while connecting to MySQL", e)
    """