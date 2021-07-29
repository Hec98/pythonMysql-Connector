import mysql.connector as mysql

miDb = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'toor',
    database = 'prueba'
)

cursor = miDb.cursor()

def dataBaseStructure():
    cursor.execute('SHOW CREATE TABLE Usuario')
    consulta = cursor.fetchall()
    print(consulta)

def selectDataBase():
    cursor.execute('SELECT * FROM Usuario')
    # resultado = cursor.fetchone()
    resultado = cursor.fetchall()
    print(resultado)

def selectLimit(limit):
    sql = 'SELECT * FROM Usuario LIMIT %s' 
    values = (limit,)
    cursor.execute(sql, values)
    # resultado = cursor.fetchone()
    resultado = cursor.fetchall()
    print(resultado)

def insertData(user, email, edad):
    sql = 'INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)'
    values = (user, email, edad)
    cursor.execute(sql, values)
    miDb.commit()
    if(cursor.rowcount == 1): print('Update query made')
    else: print('Update query not done')

def updateData(idx, user, email, edad):
    # UPDATE `prueba`.`Usuario` SET `username` = 'user1x', `email` = 'correoXx@gmail.com', `edad` = '19' WHERE (`id` = '1')
    sql = 'UPDATE Usuario SET username = %s, email = %s, edad = %s WHERE id = %s'
    values = (user, email, edad, idx)
    cursor.execute(sql, values)
    miDb.commit()
    if(cursor.rowcount == 1): print('Update query made')
    else: print('Update query not done')

def deleteData(idx):
    sql = 'DELETE FROM Usuario WHERE id = %s'
    values = (idx,)
    cursor.execute(sql, values)
    miDb.commit()
    if(cursor.rowcount == 1): print('Delete query made')
    else: print('Delete query not done')
