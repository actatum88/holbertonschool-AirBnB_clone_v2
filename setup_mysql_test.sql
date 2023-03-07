-- Crear la base de datos hbnb_test_db si no existe
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Crear el usuario hbnb_test si no existe
CREATE USER IF NOT EXISTS ‘hbnb_test’@‘localhost’ IDENTIFIED BY ‘hbnb_test_pwd’;
-- Dar todos los privilegios de hbnb_test_db al usuario hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO ‘hbnb_test’@‘localhost’;
-- Dar el privilegio SELECT de performance_schema al usuario hbnb_test
GRANT SELECT ON performance_schema.* TO ‘hbnb_test’@‘localhost’;