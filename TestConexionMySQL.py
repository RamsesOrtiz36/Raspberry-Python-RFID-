import mysql.connector

cnx = mysql.connector.connect(user='Ramses', password='1234', host='192.168.1.68', database='codigoIoT')
cnx.close()