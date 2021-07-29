import mysql.connector as mysql

miDb = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'toor',
    database = 'prueba'
)

cursor = miDb.cursor()

''' Query database structure
cursor.execute('SHOW CREATE TABLE Usuario')
consulta = cursor.fetchall()
print(consulta)
'''

''' Select
cursor.execute('select * from Usuario')
resultado = cursor.fetchone()
resultado = cursor.fetchall()
print(resultado)
'''
# Inser data
sql = 'INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)'
values = ('correoX', 'email@gmail.com', 21)

cursor.execute(sql, values)
miDb.commit()
print(cursor.rowcount)

