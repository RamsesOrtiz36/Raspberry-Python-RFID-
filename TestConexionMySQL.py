import mysql.connector

cnx = mysql.connector.connect(user='Ramses', password='Tanis36', host='192.168.1.68', database='CodigoIoT')
print("conexion realizada")
print(cnx)

print ("Cerrar conexión")
cnx.close()
print ("Conexion cerrada")