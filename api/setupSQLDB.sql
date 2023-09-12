-- Prepares a mysql database for the project
CREATE DATABASE IF NOT EXISTS HNGxS2;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'HNGx';
GRANT ALL PRIVILEGES ON `HNGxS2`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
