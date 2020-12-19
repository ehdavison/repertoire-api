DROP DATABASE IF EXISTS repertoire;
CREATE DATABASE repertoire;
CREATE USER repertoire_user WITH PASSWORD "password";
GRANT ALL PRIVILEGES ON DATABASE repertoire TO repertoire_user