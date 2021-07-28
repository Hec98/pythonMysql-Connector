import mysql.connector as mysql

miDb = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'toor',
    database = 'prueba'
)

cursor = miDb.cursor()
cursor.execute('select * from Usuario')

resultado = cursor.fetchall()

print(resultado)
