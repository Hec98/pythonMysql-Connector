## Python - mysql connector
Necessary libraries
```
pip install mysql-connector-python
```
```ssh
pip install simple-term-menu
```
![Screenshot-at-2021-07-29-22-32-20.png](https://i.postimg.cc/ZR50Kf8X/Screenshot-at-2021-07-29-22-32-20.png)
![Screenshot-at-2021-07-29-22-40-49.png](https://i.postimg.cc/sxBX5v0c/Screenshot-at-2021-07-29-22-40-49.png)
![Screenshot-at-2021-07-29-22-45-20.png](https://i.postimg.cc/TwN1yrQ1/Screenshot-at-2021-07-29-22-45-20.png)
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
  `age` int(3) DEFAULT NULL,
   PRIMARY KEY (`id`)
);
```
* Insert data
```sql
INSERT INTO Usuario (username, email, age)
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
