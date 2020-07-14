import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='sql7.freemysqlhosting.net',
                                         database='sql7354856',
                                         user='sql7354856',
                                         password='x7iHmNhExD')
    
cursor = connection.cursor()
cursor.execute("SELECT * FROM replied")
result = cursor.fetchall()
print(result[0][0])
