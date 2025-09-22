import datetime
import mysql.connector
__cnx = None
def get_sql_connection():
    print("Opening SQL connection")
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Chetu@0607',
                                  host='127.0.0.1',
                                  database='gs')
    return __cnx

