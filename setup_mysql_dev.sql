-- Create a Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Crear el usuario hbnb_dev si no existe
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
-- Dar todos los privilegios de hbnb_dev_db al usuario hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
-- Dar el privilegio SELECT de performance_schema al usuario hbnb_dev
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";

-- Create a User and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Select privleges on database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grant all privleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;

