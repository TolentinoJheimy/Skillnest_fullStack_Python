CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

CREATE TABLE IF NOT EXISTS mascotas (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NULL,
    tipo VARCHAR(100) NULL,
    color VARCHAR(100) NULL,
    created_at DATETIME NULL DEFAULT NOW(),
    updated_at DATETIME NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);
