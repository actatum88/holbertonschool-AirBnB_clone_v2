-- Create a Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a User and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--Grand privleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Select privleges on database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
