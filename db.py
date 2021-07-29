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
    for c in consulta: 
        for y in c: print(y)

def selectDataBase():
    cursor.execute('SELECT * FROM Usuario')
    # resultado = cursor.fetchone()
    resultado = cursor.fetchall()
    for r in resultado: print(r)

def selectLimit(limit):
    sql = 'SELECT * FROM Usuario LIMIT %s' 
    values = (limit,)
    cursor.execute(sql, values)
    # resultado = cursor.fetchone()
    resultado = cursor.fetchall()
    for r in resultado: print(r)

def insertData(user, email, age):
    sql = 'INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)'
    values = (user, email, age)
    cursor.execute(sql, values)
    miDb.commit()
    if(cursor.rowcount == 1): print('Update query made')
    else: print('Update query not done')

def updateData(idx, user, email, age):
    # UPDATE `prueba`.`Usuario` SET `username` = 'user1x', `email` = 'correoXx@gmail.com', `edad` = '19' WHERE (`id` = '1')
    sql = 'UPDATE Usuario SET username = %s, email = %s, edad = %s WHERE id = %s'
    values = (user, email, age, idx)
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
