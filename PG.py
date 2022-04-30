import datetime
import psycopg2 as pg
import Constants as keys

try:
    connection = pg.connect(user = keys.user,
                            password = keys.password,
                            host = keys.host,
                            port = keys.port,
                            database = keys.database)
    
    cursor = connection.cursor()
    print("Connected to PostgreSQL Server")
except:
    print("Error while connecting to PostgreSQL")


def insertData(data, table):
    for i in range(len(data)): 
        cursor.execute("INSERT INTO " + table + "(time_stamp, open_price, high, low, close_price) VALUES(%s, %s, %s, %s, %s)", (datetime.datetime.fromtimestamp(float(data[i][0]) / 1e3), float(data[i][1]), float(data[i][2]), float(data[i][3]), float(data[i][4])))
        connection.commit()
