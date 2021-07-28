## Python - mysql connector
Install mysql-connector-python
```
pip install mysql-connector-python
```
* Create database
```sql
CREATE DATABASE prueba;
```
```sql
USE prueba;
```
* Create table
```sql
CREATE TABLE `Usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `edad` int(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
));
```
* Insert data
```sql
INSERT INTO Usuario (username, email, edad)
  VALUES('user', 'correo@gmail.com', 18);
```
* Select
```sql
SELECT * FROM Usuario;
```
```sql
SELECT * FROM Usuario WHERE id = 1;
```
[![logoN1-w.png](https://i.postimg.cc/bvwkKP8Y/logoN1-w.png)](https://github.com/Hec98)
