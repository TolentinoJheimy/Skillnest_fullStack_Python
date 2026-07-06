# Sistema de Gestión de Usuarios

## Descripción

Proyecto desarrollado en Python utilizando Programación Orientada a Objetos (POO) y MySQL.

Permite iniciar sesión mediante un usuario y contraseña. Dependiendo del tipo de usuario (ADMIN o USER), el sistema mostrará diferentes opciones.

## Tecnologías utilizadas

- Python 3
- MySQL
- PyMySQL

## Instalación

1. Instalar MySQL.
2. Crear la base de datos ejecutando:

resources/crear_bd.sql

3. Poblar la base de datos ejecutando:

resources/poblar_datos.sql

4. Instalar PyMySQL

```
pip install pymysql
```

5. Configurar usuario y contraseña de MySQL en:

conexion.py

6. Ejecutar:

```
python main.py
```

## Funcionalidades

- Inicio de sesión.
- CRUD de usuarios.
- Control de permisos.
- Menú para administrador.
- Menú para usuario.
- Base de datos MySQL.
- Programación Orientada a Objetos.

## Estructura

```
sistema_usuarios/

│── main.py
│── conexion.py
│── usuario.py

├── resources
│   ├── crear_bd.sql
│   └── poblar_datos.sql

├── docs
│   └── ERD.png

└── README.md
```