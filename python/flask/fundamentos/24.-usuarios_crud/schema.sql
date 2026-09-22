CREATE DATABASE esquema_usuarios;

USE esquema_usuarios;


CREATE TABLE usuarios (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(45),

    apellido VARCHAR(45),

    email VARCHAR(45),

    created_at DATETIME,

    updated_at DATETIME

);



INSERT INTO usuarios
(
nombre,
apellido,
email,
created_at,
updated_at
)

VALUES

(
"Juan",
"Perez",
"juan@gmail.com",
NOW(),
NOW()
),

(
"Maria",
"Lopez",
"maria@gmail.com",
NOW(),
NOW()
);